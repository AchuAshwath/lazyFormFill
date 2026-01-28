# Project Summary - LazyFormFill

## Overview
LazyFormFill is a medical NLP system designed to extract structured birth history information from clinical audio recordings and text documents. It uses state-of-the-art speech-to-text and natural language processing to automate data entry for healthcare professionals.

## Key Components

### 1. Core Extraction System (`main.py`)
- **Audio to Text**: Uses Faster Whisper for speech-to-text transcription
- **Text Extraction**: Combines spaCy and regex-based approaches
- **Field Extraction**: Extracts 11 different medical fields

### 2. Source Modules (`src/`)

#### Birth History Extractor (`src/birth_history_extractor/`)
- `birth_weight.py`: Extracts birth weight in kg from text
- Supports numeric formats (3.2 kg, 3200 g)
- Supports spelled-out numbers (three point two kg)

#### Radio Extractor (`src/radio_extractor/`)
- `config.py`: Keyword mappings for categorical fields
- `spacy_extractor.py`: spaCy-based extraction
- `medspacy_extractor.py`: medSpaCy-based extraction

### 3. Data (`data/`)
- `dataset.py`: 15 test cases with expected outputs
- Sample diagnosis texts for testing and benchmarking

### 4. Tests (`tests/`)
- `test_extractor.py`: Benchmarking and accuracy tests
- Compares spaCy vs medSpaCy approaches
- Evaluates extraction accuracy

### 5. Examples (`examples/`)
- `basic_text_extraction.py`: Simple extraction examples
- `dataset_processing.py`: Batch processing with accuracy metrics

### 6. Docker Support (`docker-files/`)
- Docker Compose configuration
- Easy deployment and containerization

## Extracted Fields

1. **conception_mode**: Natural or Assisted (IVF/ART)
2. **delivery_mode**: NVD (Normal Vaginal Delivery) or LSCS (Cesarean)
3. **term**: Term or Preterm
4. **cried_at_birth**: Yes or No
5. **birth_weight**: Float value in kilograms
6. **pedigree**: Family history information
7. **consanguinity**: Consanguinity status
8. **antenatal_history**: Pregnancy history
9. **perinatal_history**: Birth-related events
10. **postnatal_complications**: Post-birth complications
11. **breastfed_upto**: Breastfeeding duration

## Technical Architecture

### NLP Pipeline
1. **Audio Input** → Faster Whisper → Transcribed Text
2. **Text Input** → spaCy NLP Processing → Tokenization & POS Tagging
3. **Pattern Matching** → PhraseMatcher + Regex → Field Extraction
4. **Disambiguation** → Context Analysis → Final Values

### Extraction Methods
- **spaCy PhraseMatcher**: Fast pattern matching for known phrases
- **Regex Fallback**: Catches patterns missed by spaCy
- **Context Analysis**: Disambiguates terms like "assisted"
- **Negation Handling**: Detects negations for "cried_at_birth"

## Documentation Structure

```
├── README.md              # Main documentation with overview
├── QUICKSTART.md          # 5-minute setup guide
├── API.md                 # Detailed API reference
├── CONTRIBUTING.md        # Contribution guidelines
├── CHANGELOG.md           # Version history
├── LICENSE                # MIT License
├── docs/
│   └── DOCKER.md          # Docker deployment guide
└── examples/
    └── README.md          # Examples documentation
```

## Development Highlights

### Package Structure
- Proper Python package with `__init__.py` files
- Clear module organization
- Type hints for better code clarity

### Dependencies Management
- `pyproject.toml`: Main project configuration
- `requirements.txt`: Pip-compatible dependencies
- `uv.lock`: Locked dependencies for reproducibility

### Code Quality
- Comprehensive docstrings
- Type hints
- Modular design
- Clear separation of concerns

## Use Cases

1. **Healthcare Data Entry**: Automate birth history documentation
2. **Medical Record Digitization**: Convert audio notes to structured data
3. **Clinical Research**: Extract data from medical narratives
4. **EMR Integration**: Populate electronic medical records
5. **Quality Assurance**: Validate manually entered data

## Performance

- **Text Extraction**: < 1 second per document
- **Audio Transcription**: Depends on model size (small model recommended for balance)
- **Accuracy**: Benchmarked against test dataset (see examples)

## Future Enhancements

1. Web API for easy integration
2. Multi-language support
3. Real-time streaming transcription
4. Enhanced medical entity recognition
5. Database integration
6. GUI interface
7. Support for more medical specialties

## Technology Stack

- **Language**: Python 3.9+
- **Speech Recognition**: Faster Whisper
- **NLP**: spaCy, medSpaCy
- **Numerical**: NumPy
- **Text Processing**: Regex, word2number
- **Containerization**: Docker

## Getting Started

See [QUICKSTART.md](QUICKSTART.md) for a 5-minute setup guide.

## Repository Structure

```
lazyFormFill/
├── main.py                   # Main entry point
├── src/                      # Source modules
├── data/                     # Test datasets
├── tests/                    # Test suite
├── examples/                 # Usage examples
├── docs/                     # Additional documentation
├── docker-files/             # Docker configuration
└── dev/                      # Development experiments
```

## License

MIT License - See [LICENSE](LICENSE) file for details.

---

**Repository**: https://github.com/AchuAshwath/lazyFormFill
**Last Updated**: 2024-01-28
