# API Documentation

This document provides detailed information about the LazyFormFill API and its functions.

## Table of Contents

1. [Main Extraction Functions](#main-extraction-functions)
2. [Audio Processing](#audio-processing)
3. [Field Extractors](#field-extractors)
4. [Configuration](#configuration)

---

## Main Extraction Functions

### `extract_birth_history_from_audio(audio_file: str) -> dict`

Extracts birth history fields from an audio file using Faster Whisper and NLP extraction.

**Parameters:**
- `audio_file` (str): Path to the audio file (supports .m4a, .mp3, .wav, etc.)

**Returns:**
- `dict`: Dictionary containing extracted birth history fields

**Fields Extracted:**
- `conception_mode`: "Natural" or "Assisted"
- `delivery_mode`: "NVD" or "LSCS"
- `term`: "Term" or "Preterm"
- `cried_at_birth`: "Yes" or "No"
- `birth_weight`: float (in kg)
- `pedigree`: str or None
- `consanguinity`: str or None
- `antenatal_history`: str or None
- `perinatal_history`: str or None
- `postnatal_complications`: str or None
- `breastfed_upto`: str or None

**Example:**
```python
from main import extract_birth_history_from_audio

result = extract_birth_history_from_audio("recording.m4a")
print(result)
# {
#   'conception_mode': 'Natural',
#   'delivery_mode': 'LSCS',
#   'term': 'Term',
#   'cried_at_birth': 'Yes',
#   'birth_weight': 3.2,
#   ...
# }
```

**Notes:**
- Requires Faster Whisper model to be installed
- First run may take longer due to model loading
- Audio quality affects transcription accuracy

---

### `extract_birth_history_from_dataset(text: str) -> dict`

Extracts birth history fields from clinical text.

**Parameters:**
- `text` (str): Clinical text containing birth history information

**Returns:**
- `dict`: Dictionary containing extracted birth history fields (same structure as above)

**Example:**
```python
from main import extract_birth_history_from_dataset

text = """
Patient was born at term via NVD. Birth weight was 3.2 kg.
The baby cried immediately after birth.
"""

result = extract_birth_history_from_dataset(text)
print(result)
```

**Notes:**
- Works with raw clinical text
- Case-insensitive matching
- Handles various medical terminologies

---

## Audio Processing

### `transcribe_audio(audio_file: str) -> Iterator[Segment]`

Transcribes audio file using Faster Whisper model.

**Parameters:**
- `audio_file` (str): Path to audio file

**Returns:**
- `Iterator[Segment]`: Iterator of transcription segments

**Example:**
```python
from main import transcribe_audio

segments = transcribe_audio("audio.m4a")
full_text = " ".join([seg.text for seg in segments])
print(full_text)
```

**Configuration:**
- Model size: Configurable (default: "small")
- Device: CPU with int8 compute type
- Beam size: 5

---

## Field Extractors

### Radio Field Extraction

#### `extract_radio_fields(text: str) -> dict`

Extracts categorical/radio button fields from text using spaCy PhraseMatcher.

**Parameters:**
- `text` (str): Clinical text

**Returns:**
- `dict`: Dictionary with radio field values

**Fields:**
- `conception_mode`
- `delivery_mode`
- `term`
- `cried_at_birth`

**Example:**
```python
from main import extract_radio_fields

text = "Baby was delivered via caesarean section"
result = extract_radio_fields(text)
# {'delivery_mode': 'LSCS'}
```

---

### Birth Weight Extraction

#### `extract_birth_weight(text: str) -> float`

Extracts birth weight from clinical text.

**Parameters:**
- `text` (str): Text containing birth weight information

**Returns:**
- `float`: Birth weight in kilograms, or None if not found

**Supported Formats:**
- Numeric: "3.2 kg", "3200 g", "3.2 kilograms"
- Spelled out: "three point two kg" (requires word2number)

**Example:**
```python
from src.birth_history_extractor import extract_birth_weight

text = "Birth weight was 3.2 kg"
weight = extract_birth_weight(text)
print(weight)  # 3.2

text = "Birth weight: 3200 grams"
weight = extract_birth_weight(text)
print(weight)  # 3.2
```

---

### Other Field Extractors

#### `extract_pedigree_regex(text: str) -> str`
Extracts family history/pedigree information.

#### `extract_consanguinity_regex(text: str) -> str`
Extracts consanguinity information.

#### `extract_antenatal_history_regex(text: str) -> str`
Extracts antenatal history.

#### `extract_perinatal_history_regex(text: str) -> str`
Extracts perinatal history.

#### `extract_postnatal_complications_regex(text: str) -> str`
Extracts postnatal complications.

#### `extract_breastfed_upto_regex(text: str) -> str`
Extracts breastfeeding duration.

**Example:**
```python
from main import extract_other_fields

text = "Antenatal history was uneventful. No postnatal complications."
result = extract_other_fields(text)
# {
#   'pedigree': None,
#   'consanguinity': None,
#   'antenatal_history': 'uneventful',
#   'perinatal_history': None,
#   'postnatal_complications': 'no postnatal complications',
#   'breastfed_upto': None
# }
```

---

## Configuration

### Keyword Mappings (`src/radio_extractor/config.py`)

The `KEYWORD_MAP` dictionary defines synonyms for radio field values:

```python
KEYWORD_MAP = {
    "conception_mode": {
        "natural": "Natural",
        "ivf": "Assisted",
        "art": "Assisted",
        # ... more synonyms
    },
    "delivery_mode": {
        "nvd": "NVD",
        "cesarean": "LSCS",
        "c-section": "LSCS",
        # ... more synonyms
    },
    "term": {
        "term": "Term",
        "full-term": "Term",
        "preterm": "Preterm",
        "premature": "Preterm",
        # ... more synonyms
    },
    "cried_at_birth": {
        "cried": "Yes",
        "cried immediately": "Yes",
        "did not cry": "No",
        "no cry": "No",
        # ... more synonyms
    }
}
```

**Customization:**
You can add new synonyms or modify existing ones by editing this file.

---

### Context Keywords

Used for disambiguating terms like "assisted":

```python
CONTEXT_KEYWORDS = {
    "conception_mode": ["conceived", "fertilization", "art"],
    "delivery_mode": ["deliver", "delivery", "section", "vaginal"],
}
```

---

## Error Handling

All extraction functions gracefully handle errors:
- Missing fields return `None`
- Invalid formats are skipped
- Extraction continues even if some fields fail

**Example:**
```python
result = extract_birth_history_from_dataset("minimal text")
# Returns all fields with None for unextracted fields
```

---

## Performance Considerations

### Audio Transcription
- **Small model**: ~500MB, faster, good accuracy
- **Medium model**: ~1.5GB, slower, better accuracy
- **Large model**: ~3GB, slowest, best accuracy

### Text Extraction
- Fast processing (< 1 second for typical clinical notes)
- Parallel processing supported for batch operations

---

## Type Hints

The codebase uses type hints for better IDE support:

```python
def extract_birth_weight(text: str) -> float:
    ...

def extract_radio_fields(text: str) -> dict:
    ...
```

---

## Dependencies

Key dependencies and their purposes:

- **faster-whisper**: Speech-to-text transcription
- **spacy**: NLP and pattern matching
- **medspacy**: Medical text processing
- **word2number**: Convert spelled numbers to digits
- **numpy**: Numerical operations

---

## Testing

Test your extractions:

```python
from tests.test_extractor import evaluate, benchmark_cases
from main import extract_birth_history_from_dataset

accuracy, time = evaluate(extract_birth_history_from_dataset, benchmark_cases)
print(f"Accuracy: {accuracy:.2f}%")
print(f"Time: {time:.4f}s")
```

---

For more examples, see the `examples/` directory.
