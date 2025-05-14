import time
import re
from faster_whisper import WhisperModel
import spacy
from spacy.matcher import PhraseMatcher
# from radio_extractor.config import KEYWORD_MAP
from word2number import w2n  # Assuming you have word2number for spelled-out numbers


KEYWORD_MAP = {
  "conception_mode": {
    "natural":        "Natural",
    "naturally":      "Natural",
    "spontaneous":    "Natural",
    "assisted":       "Assisted",
    "ivf":            "Assisted",
    "IVF":           "Assisted",
    "in vitro fertilization": "Assisted",
    "art":            "Assisted",
    "assisted reproductive technology": "Assisted",
  },
  "delivery_mode": {
    "delivery was normal" : "NVD",
    "conceived naturally" : "NVD",
    "nvd":            "NVD",
    "normal vaginal": "NVD",
    "spontaneous vaginal": "NVD",
    "vaginal delivery":   "NVD",
    "vaginal":       "NVD",
    "cesarean":      "LSCS",
    "caesarean":     "LSCS",
    "c section":     "LSCS",
    "c-section":     "LSCS",
    "csection":      "LSCS",
    "elective c-section": "LSCS",
    "surgical delivery":  "LSCS",
    "abdominal delivery": "LSCS",
    "assisted":      "Assisted",
    "lscs":          "LSCS",         # <- ADDED
    "lower segment caesarean": "LSCS"
  },
  "term": {
    "term":          "Term",
    "full-term":     "Term",
    "full term":     "Term",
    "at term":       "Term",
    "delivered at term": "Term",     # <- ADDED
    "preterm":       "Preterm",
    "premature":     "Preterm",
    "premature birth":"Preterm",
    "preemie":       "Preterm",
    "premo":         "Preterm",
  },
  "cried_at_birth": {
    "cried":             "Yes",
    "cried immediately": "Yes",
    "cried vigorously":  "Yes",
    "did not cry":       "No",
    "didn't cry":        "No",
    "failed to cry":     "No",
    "no cry":            "No",
    "apgar 0":           "No",
  }
}


# Initialize Faster Whisper for Speech-to-Text
def transcribe_audio(audio_file: str):
    """Transcribe audio file using Faster Whisper."""
    model_size = "small"
    whisper_model = WhisperModel(model_size, device="cpu", compute_type="int8")

    stt_start = time.time()
    segments, info = whisper_model.transcribe(audio_file, beam_size=5)
    stt_end = time.time()

    print(f"Transcription took {stt_end - stt_start:.2f} seconds")
    return segments

# Initialize spaCy and set up PhraseMatcher
nlp = spacy.load("en_core_web_sm")
nlp.add_pipe("sentencizer", first=True)
matcher = PhraseMatcher(nlp.vocab, attr="LOWER")

# Build PhraseMatcher for all radio fields
for field, synonyms in KEYWORD_MAP.items():
    patterns = [nlp.make_doc(expr) for expr in synonyms.keys()]
    matcher.add(field, patterns)

# Context keywords for disambiguation of 'assisted'
CONTEXT_KEYWORDS = {
    "conception_mode": ["conceived", "fertilization", "art"],
    "delivery_mode": ["deliver", "delivery", "section", "vaginal"],
}

# Regex fallback for radio fields
REGEX_PATTERNS = {}
for field, synonyms in KEYWORD_MAP.items():
    keys = sorted(synonyms.keys(), key=lambda x: -len(x))
    pattern = r"\b(?:" + r"|".join(re.escape(k) for k in keys) + r")\b"
    REGEX_PATTERNS[field] = re.compile(pattern, re.IGNORECASE)

# Extract radio fields using spaCy PhraseMatcher and regex fallback
def extract_radio_fields(text: str) -> dict:
    """Extracts radio fields from the given text using spaCy and regex."""
    results = {}
    doc = nlp(text)
    matches = matcher(doc)

    # 1. spaCy-based extraction
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
        if option:
            # Disambiguate 'assisted'
            if span_text == "assisted" and not any(ctx in sent_text for ctx in CONTEXT_KEYWORDS.get(field, [])):
                continue
            results[field] = option

    # 2. Regex fallback for missing fields
    for field, pattern in REGEX_PATTERNS.items():
        if field not in results:
            m = pattern.search(text)
            if m:
                key = m.group(0).lower()
                results[field] = KEYWORD_MAP[field].get(key)
    return results

# Extract birth weight using regex
def extract_birth_weight(text: str) -> float:
    """Extracts birth weight from the given text using regex."""
    numeric_match = re.search(
        r'(\d+(?:[\d,]*)(?:\.\d+)?)\s*(kg|kilograms|g|grams|kilos)',
        text,
        re.IGNORECASE
    )
    if numeric_match:
        value = float(numeric_match.group(1).replace(',', ''))
        unit = numeric_match.group(2).lower()
        if unit in ['g', 'grams']:
            value = value / 1000
        return value

    if w2n:
        spelled_match = re.search(
            r'([a-z\s\-\d]+?)\s*(kg|kilograms|kilos)',
            text,
            re.IGNORECASE
        )
        if spelled_match:
            words = spelled_match.group(1)
            try:
                num = w2n.word_to_num(words)
                return float(num)
            except Exception:
                pass
    return None

def extract_pedigree_regex(text: str) -> str:
    """Extracts pedigree information from the given text using regex."""
    m = re.search(r'(?:pedigree[:\s]*no|family history is negative for|pedigree was|pedigree|family history|lineage| genetic)\s*([\w\s-]+?)(?:;|\.|$)', text, re.IGNORECASE)
    if m:
        clause = m.group(1).strip().lower()
        return clause if 'negative for' in m.group(0).lower() or 'unremarkable' in m.group(0).lower() else f"no {clause}"
    return None


def extract_consanguinity_regex(text: str) -> str:
    """Extracts consanguinity information from the given text using regex."""
    m = re.search(r'\b(no history of consanguinity|parents are unrelated|no consanguinity reported|cousin marriage)\b', text, re.IGNORECASE)
    return m.group(1).lower() if m else None


def extract_antenatal_history_regex(text: str) -> str:
    """Extracts antenatal history from the given text using regex."""
    m = re.search(r'antenatal (?:history|period)(?: was|:)?\s*(.*?)(?:\.|$)', text, re.IGNORECASE)
    return m.group(1).strip().lower() if m else None


def extract_perinatal_history_regex(text: str) -> str:
    """Extracts perinatal history from the given text using regex."""
    m = re.search(r'perinatal (?:history:|events )?\s*(.*?)(?:\.|$)', text, re.IGNORECASE)
    return m.group(1).strip().lower() if m else None


def extract_postnatal_complications_regex(text: str) -> str:
    """Extracts postnatal complications from the given text using regex."""
    m = re.search(r'\bno postnatal complications\b', text, re.IGNORECASE)
    if m:
        return m.group(0).lower()
    m = re.search(r'postnatal (?:complications[:]?|)\s*(?:occurred\s*)?(.*?)(?:\.|$)', text, re.IGNORECASE)
    return m.group(1).strip().lower() if m else None


def extract_breastfed_upto_regex(text: str) -> str:
    """Extracts breastfed information from the given text using regex."""
    m = re.search(r'\b(?:breastfed|breastfeeding)\s*(?:the infant )?(?:exclusively )?(?:up to|for|continued for|was continued)\s*([\w\s]+?)(?:months?|days?|years?|mos|yrs|\.|$)', text, re.IGNORECASE)
    return m.group(1).strip().lower() + " months" if m else None

# Extract other fields using regex
def extract_other_fields(text: str) -> dict:
    """Extracts other fields from the given text using regex."""
    return {
        "pedigree": extract_pedigree_regex(text),
        "consanguinity": extract_consanguinity_regex(text),
        "antenatal_history": extract_antenatal_history_regex(text),
        "perinatal_history": extract_perinatal_history_regex(text),
        "postnatal_complications": extract_postnatal_complications_regex(text),
        "breastfed_upto": extract_breastfed_upto_regex(text),
    }

# Function to combine all extraction methods into one pipeline
def extract_birth_history_from_audio(audio_file: str):
    """
    Extracts birth history fields from an audio file using Faster Whisper and regex.
    """
    # Step 1: Transcribe audio
    segments = transcribe_audio(audio_file)
    
    # Step 2: Combine all text segments into a single string
    full_text = " ".join([segment.text for segment in segments])
    print(f"Transcribed text: {full_text}")
    print("---------------------------------------------------------------------------------------------------------")
    print()

    # Step 3: Extract relevant fields using all extraction methods
    birth_history = {}
    birth_history.update(extract_radio_fields(full_text))
    birth_history["birth_weight"] = extract_birth_weight(full_text)
    birth_history.update(extract_other_fields(full_text))

    return birth_history

def extract_birth_history_from_dataset(text: str):
    """
    Extracts birth history fields from a given text string.
    """    
    birth_history = {}
    birth_history.update(extract_radio_fields(text))
    birth_history["birth_weight"] = extract_birth_weight(text)
    birth_history.update(extract_other_fields(text))
    return birth_history


if __name__ == "__main__":
    # Example usage
    audio_file = "Recording (2).m4a"
    birth_history = extract_birth_history_from_audio(audio_file)

    print(birth_history)

# for entry in Dataset:
#     full_text = entry["diagnosis_text"]
#     # extract_birth_history_from_dataset(full_text)
#     birth_history = extract_birth_history_from_dataset(full_text)
    
#     print(entry['diagnosis_text'])
#     print()
#     print(birth_history)

    
    
#     print("---------------------------------------------------------------------------------------------------------")
       
