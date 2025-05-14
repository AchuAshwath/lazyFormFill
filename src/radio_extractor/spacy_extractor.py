import spacy
from spacy.matcher import PhraseMatcher
from config import KEYWORD_MAP

# Load a lightweight English model
nlp = spacy.load("en_core_web_sm")

# Build PhraseMatcher patterns for each field
matcher = PhraseMatcher(nlp.vocab, attr="LOWER")
for field, synonyms in KEYWORD_MAP.items():
    patterns = [nlp.make_doc(expr) for expr in synonyms.keys()]
    matcher.add(field, patterns)


def extract_radio_fields(text: str) -> dict:
    """
    Pure spaCy extractor for radio-button fields via PhraseMatcher.
    Returns a dict with field:value mappings (first hit per field).
    """
    doc = nlp(text)
    results = {}
    for match_id, start, end in matcher(doc):
        field = nlp.vocab.strings[match_id]
        span_text = doc[start:end].text.lower()
        if field not in results:
            results[field] = KEYWORD_MAP[field].get(span_text)
    return results
