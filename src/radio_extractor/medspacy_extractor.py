# File: radio_extractor.py
# Extracts categorical radio fields (conception_mode, delivery_mode, term, cried_at_birth)
# Uses spaCy + PhraseMatcher if available, otherwise falls back to regex lookup

import re
from radio_extractor.config import KEYWORD_MAP

# Try to import spaCy and set up PhraseMatcher
try:
    import spacy
    from spacy.matcher import PhraseMatcher
    SPACY_AVAILABLE = True
except ImportError:
    SPACY_AVAILABLE = False

if SPACY_AVAILABLE:
    # Initialize spaCy and Sentence segmentation
    nlp = spacy.load("en_core_web_sm")
    nlp.add_pipe("sentencizer", first=True)
    
    # Build PhraseMatcher for all radio fields
    matcher = PhraseMatcher(nlp.vocab, attr="LOWER")
    for field, synonyms in KEYWORD_MAP.items():
        patterns = [nlp.make_doc(expr) for expr in synonyms.keys()]
        matcher.add(field, patterns)

# Context keywords for disambiguation of 'assisted'
CONTEXT_KEYWORDS = {
    "conception_mode": ["conceived", "fertilization", "art"],
    "delivery_mode": ["deliver", "delivery", "section", "vaginal"],
}

# Regex fallback: pre-compile patterns for each field
REGEX_PATTERNS = {}
for field, synonyms in KEYWORD_MAP.items():
    keys = sorted(synonyms.keys(), key=lambda x: -len(x))
    pattern = r"\b(?:" + r"|".join(re.escape(k) for k in keys) + r")\b"
    REGEX_PATTERNS[field] = re.compile(pattern, re.IGNORECASE)


def extract_radio_fields(text: str) -> dict:
    """
    Extract radio fields mapping to their normalized values.
    First uses spaCy PhraseMatcher on full doc to respect context and negation.
    Falls back to regex scan over full text for any missing fields.
    """
    results = {}
    # 1. spaCy-based extraction
    if SPACY_AVAILABLE:
        doc = nlp(text)
        matches = matcher(doc)
        for match_id, start, end in matches:
            field = doc.vocab.strings[match_id]
            span = doc[start:end]
            span_text = span.text.lower().strip()
            sent = span.sent
            sent_text = sent.text.lower()
            # Handle negation for 'cried_at_birth'
            if field == "cried_at_birth":
                neg = bool(re.search(r"\b(did not cry|didn't cry|failed to cry|no cry)\b", sent_text))
                results[field] = "No" if neg else "Yes"
                continue
            # Map only if synonym in map
            option = KEYWORD_MAP[field].get(span_text)
            if not option:
                continue
            # Disambiguate 'assisted'
            if span_text == "assisted":
                if not any(ctx in sent_text for ctx in CONTEXT_KEYWORDS.get(field, [])):
                    continue
            if field not in results:
                results[field] = option
    # 2. Regex fallback for missing fields
    for field, pattern in REGEX_PATTERNS.items():
        if field not in results:
            m = pattern.search(text)
            if m:
                key = m.group(0).lower()
                results[field] = KEYWORD_MAP[field].get(key)
    return results

# Alias for backward compatibility
extract_radio_fields_medspacy = extract_radio_fields


if __name__ == '__main__':
    sample = (
        "The infant was conceived naturally after spontaneous fertilization, "
        "delivered by c-section at full term. The baby cried vigorously at birth."
    )
    print("Sample Text:\n", sample)
    print("\nExtracted Radio Fields:")
    print(extract_radio_fields(sample))
