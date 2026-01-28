# Quick Start Guide

Get started with LazyFormFill in 5 minutes!

## 1. Install Dependencies

```bash
# Clone the repository
git clone https://github.com/AchuAshwath/lazyFormFill.git
cd lazyFormFill

# Create virtual environment
python -m venv .venv
source .venv/bin/activate  # On Windows: .venv\Scripts\activate

# Install dependencies
pip install -r requirements.txt

# Download spaCy model
python -m spacy download en_core_web_sm
```

## 2. Extract from Text (Quickest)

```python
from main import extract_birth_history_from_dataset

text = """
Baby delivered at term via caesarean section. 
Birth weight was 3.2 kg. 
The baby cried immediately after birth.
"""

result = extract_birth_history_from_dataset(text)
print(result)
```

**Output:**
```python
{
  'conception_mode': None,
  'delivery_mode': 'LSCS',
  'term': 'Term',
  'cried_at_birth': 'Yes',
  'birth_weight': 3.2,
  'pedigree': None,
  'consanguinity': None,
  'antenatal_history': None,
  'perinatal_history': None,
  'postnatal_complications': None,
  'breastfed_upto': None
}
```

## 3. Extract from Audio

```python
from main import extract_birth_history_from_audio

# Place your audio file in the project directory
audio_file = "recording.m4a"

result = extract_birth_history_from_audio(audio_file)
print(result)
```

## 4. Run Examples

```bash
# Basic text extraction
python examples/basic_text_extraction.py

# Process dataset with accuracy metrics
python examples/dataset_processing.py
```

## 5. Test the System

```bash
# Run tests
python tests/test_extractor.py
```

## Common Issues

### Issue: spaCy model not found
**Solution:**
```bash
python -m spacy download en_core_web_sm
```

### Issue: ImportError for word2number
**Solution:**
```bash
pip install word2number
```

### Issue: Audio transcription fails
**Solution:** Make sure you have the faster-whisper package:
```bash
pip install faster-whisper
```

## Next Steps

- Read the [full README](README.md) for detailed documentation
- Check out [API documentation](API.md) for function references
- See [examples](examples/) for more use cases
- Learn about [Docker deployment](docs/DOCKER.md)

## Getting Help

- Open an issue on [GitHub](https://github.com/AchuAshwath/lazyFormFill/issues)
- Check existing issues for solutions
- Read the [Contributing Guide](CONTRIBUTING.md)

---

**Ready to go!** 🚀
