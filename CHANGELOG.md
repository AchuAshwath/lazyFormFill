# Changelog

All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.0.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [0.1.0] - 2024-01-28

### Added
- Initial release of LazyFormFill
- Audio transcription using Faster Whisper
- Birth history extraction from clinical text
- Support for multiple extraction methods (spaCy and medSpaCy)
- Field extraction for:
  - Conception mode (Natural/Assisted)
  - Delivery mode (NVD/LSCS)
  - Term (Preterm/Term)
  - Birth weight (kg)
  - Crying at birth (Yes/No)
  - Pedigree information
  - Consanguinity status
  - Antenatal history
  - Perinatal history
  - Postnatal complications
  - Breastfeeding duration
- Comprehensive README with installation and usage instructions
- Example scripts for text extraction and dataset processing
- Docker support with docker-compose configuration
- Test suite with benchmark cases
- API documentation
- Contributing guidelines
- MIT License

### Technical Features
- Python package structure with proper __init__.py files
- Type hints for better code clarity
- Regex-based fallback extraction
- PhraseMatcher for efficient pattern matching
- Context-aware disambiguation
- Support for multiple medical terminologies

### Documentation
- Comprehensive README.md
- API.md for detailed API reference
- CONTRIBUTING.md with contribution guidelines
- Examples directory with working code samples
- Inline code documentation and docstrings

### Testing
- Test suite for extraction accuracy
- Benchmark cases for performance evaluation
- Sample dataset with 15 test cases

## [Unreleased]

### Planned Features
- Web API for easy integration
- Support for more audio formats
- Multi-language support
- Real-time streaming transcription
- Enhanced medical entity recognition
- Database integration
- GUI interface
- Improved accuracy with transformer models
- Batch processing utilities
- Export to various formats (JSON, CSV, XML)

---

For detailed changes, see the [commit history](https://github.com/AchuAshwath/lazyFormFill/commits/main).
