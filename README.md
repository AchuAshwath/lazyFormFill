# LazyFormFill - Medical Birth History Extraction System

[![Python 3.9+](https://img.shields.io/badge/python-3.9+-blue.svg)](https://www.python.org/downloads/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

An intelligent NLP-based system for extracting structured birth history information from clinical audio recordings and text documents. This project combines speech-to-text technology with advanced natural language processing to automatically extract medical information such as delivery mode, conception method, birth weight, and other critical birth history fields.

## 🎯 Overview

LazyFormFill automates the extraction of birth history data from medical narratives, significantly reducing manual data entry time for healthcare professionals. The system uses:

- **Speech-to-Text**: Faster Whisper model for accurate audio transcription
- **NLP Extraction**: spaCy and medSpaCy for medical entity recognition
- **Pattern Matching**: Regex-based extraction for specific medical fields

## ✨ Features

- 🎤 **Audio Transcription**: Convert medical audio recordings to text using Faster Whisper
- 📝 **Text Extraction**: Extract birth history from clinical text documents
- 🏥 **Medical Field Detection**: Automatically identify and extract:
  - Conception mode (Natural/Assisted)
  - Delivery mode (NVD/LSCS)
  - Term (Preterm/Term)
  - Birth weight (in kg)
  - Crying at birth (Yes/No)
  - Pedigree information
  - Consanguinity status
  - Antenatal history
  - Perinatal history
  - Postnatal complications
  - Breastfeeding duration
- 🔍 **Multiple Extraction Methods**: Uses both spaCy and medSpaCy approaches for improved accuracy
- 🐳 **Docker Support**: Easy deployment with Docker Compose

## 🛠️ Technology Stack

- **Python 3.9+**
- **Faster Whisper**: Speech-to-text transcription
- **spaCy**: Natural language processing
- **medSpaCy**: Medical-specific NLP extensions
- **NumPy**: Numerical computations
- **word2number**: Converts spelled-out numbers to digits
- **Docker**: Containerization support

## 📋 Prerequisites

- Python 3.9 or higher
- Docker and Docker Compose (optional, for containerized deployment)
- Sufficient disk space for Whisper models (~500MB for small model)

## 🚀 Installation

### Option 1: Using uv (Recommended)

```bash
# Clone the repository
git clone https://github.com/AchuAshwath/lazyFormFill.git
cd lazyFormFill

# Install uv if you haven't already
curl -LsSf https://astral.sh/uv/install.sh | sh

# Create virtual environment and install dependencies
uv venv
source .venv/bin/activate  # On Windows: .venv\Scripts\activate

# Install dependencies
uv pip install -e .
```

### Option 2: Using pip

```bash
# Clone the repository
git clone https://github.com/AchuAshwath/lazyFormFill.git
cd lazyFormFill

# Create virtual environment
python -m venv .venv
source .venv/bin/activate  # On Windows: .venv\Scripts\activate

# Install dependencies
pip install -r requirements.txt
```

### Install spaCy Language Model

```bash
# Download the English language model
python -m spacy download en_core_web_sm
```

### Option 3: Using Docker

```bash
# Clone the repository
git clone https://github.com/AchuAshwath/lazyFormFill.git
cd lazyFormFill/docker-files

# Build and run with Docker Compose
docker-compose up -d
```

## 📖 Usage

### Extract Birth History from Audio

```python
from main import extract_birth_history_from_audio

# Path to your audio file (supports .m4a, .mp3, .wav)
audio_file = "path/to/medical_recording.m4a"

# Extract birth history
birth_history = extract_birth_history_from_audio(audio_file)

print(birth_history)
# Output: {
#   'conception_mode': 'Natural',
#   'delivery_mode': 'LSCS',
#   'term': 'Term',
#   'cried_at_birth': 'Yes',
#   'birth_weight': 3.2,
#   'pedigree': 'family history of diabetes',
#   'consanguinity': None,
#   'antenatal_history': 'gestational diabetes',
#   'perinatal_history': None,
#   'postnatal_complications': None,
#   'breastfed_upto': '6 months'
# }
```

### Extract Birth History from Text

```python
from main import extract_birth_history_from_dataset

# Your clinical text
text = """
A 4-year-old child with a family history of diabetes. 
The child was conceived naturally and delivered by caesarean section at 38 weeks. 
The baby cried immediately after birth. Birth weight was 3.2 kg.
There were no postnatal complications, and breastfeeding continued for 4 months.
"""

# Extract birth history
birth_history = extract_birth_history_from_dataset(text)

print(birth_history)
```

### Running the Main Script

```bash
# Run the extraction on a sample audio file
python main.py
```

## 📁 Project Structure

```
lazyFormFill/
├── main.py                          # Main extraction pipeline
├── pyproject.toml                   # Project dependencies
├── uv.lock                          # Dependency lock file
├── .gitignore                       # Git ignore rules
├── .python-version                  # Python version specification
│
├── src/                             # Source code
│   ├── birth_history_extractor/     # Birth history extraction modules
│   │   └── birth_weight.py          # Birth weight extraction logic
│   │
│   └── radio_extractor/             # Radio field extraction modules
│       ├── config.py                # Keyword mappings and configuration
│       ├── spacy_extractor.py       # spaCy-based extraction
│       └── medspacy_extractor.py    # medSpaCy-based extraction
│
├── data/                            # Data files
│   └── dataset.py                   # Sample dataset for testing
│
├── tests/                           # Test files
│   ├── test_extractor.py            # Extraction benchmarking tests
│   ├── test_birth_history_examples.py  # Example test cases
│   └── birthHistory_testCases.py    # Birth history test cases
│
├── docker-files/                    # Docker configuration
│   ├── docker-compose.yml           # Docker Compose configuration
│   └── entrypoint.sh                # Docker entrypoint script
│
└── dev/                             # Development files
    ├── whisper.py                   # Whisper model experiments
    ├── seellama_infer.py            # LLM inference experiments
    └── medsapcy.ipynb               # medSpaCy experiments notebook
```

## 🧪 Testing

Run the test suite to verify the extraction accuracy:

```bash
# Run all tests
python -m pytest tests/

# Run specific test
python tests/test_extractor.py

# Run benchmarking tests
python tests/test_extractor.py
```

The benchmarking tests compare the accuracy and speed of different extraction methods (pure spaCy vs. medSpaCy).

## 🔧 Configuration

### Keyword Mappings

The system uses keyword mappings defined in `src/radio_extractor/config.py`. You can customize these mappings to:

- Add new synonyms for existing fields
- Add support for different medical terminologies
- Adjust extraction rules

Example:
```python
KEYWORD_MAP = {
  "conception_mode": {
    "natural": "Natural",
    "ivf": "Assisted",
    # Add more synonyms...
  },
  # Add more field mappings...
}
```

### Whisper Model Configuration

You can change the Whisper model size in `main.py`:

```python
model_size = "small"  # Options: "tiny", "base", "small", "medium", "large"
```

Larger models provide better accuracy but require more resources.

## 🐳 Docker Deployment

The project includes Docker support for easy deployment:

```bash
cd docker-files
docker-compose up -d
```

This will:
1. Pull the Faster Whisper Docker image
2. Mount your project directory
3. Configure the Whisper model (default: small)
4. Expose the service on port 10300

## 🤝 Contributing

Contributions are welcome! Please feel free to submit a Pull Request. For major changes:

1. Fork the repository
2. Create your feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

## 📝 License

This project is licensed under the MIT License - see the LICENSE file for details.

## 🙏 Acknowledgments

- [Faster Whisper](https://github.com/guillaumekln/faster-whisper) for efficient speech-to-text
- [spaCy](https://spacy.io/) for NLP capabilities
- [medSpaCy](https://github.com/medspacy/medspacy) for medical text processing

## 📧 Contact

For questions or feedback, please open an issue on GitHub.

## 🔮 Future Enhancements

- [ ] Web API for easy integration
- [ ] Support for more audio formats
- [ ] Multi-language support
- [ ] Real-time streaming transcription
- [ ] Enhanced medical entity recognition
- [ ] Database integration for storing extracted data
- [ ] GUI for easier interaction

---

**Note**: This is a testing/development version. Please validate all extracted information before using in production medical environments.
