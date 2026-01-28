# Contributing to LazyFormFill

Thank you for your interest in contributing to LazyFormFill! This document provides guidelines for contributing to the project.

## How to Contribute

### Reporting Bugs

If you find a bug, please open an issue on GitHub with:
- A clear description of the bug
- Steps to reproduce the issue
- Expected behavior vs actual behavior
- Your environment (OS, Python version, etc.)
- Any relevant error messages or logs

### Suggesting Enhancements

We welcome suggestions for new features or improvements! Please open an issue with:
- A clear description of the enhancement
- Use cases and benefits
- Any implementation ideas you might have

### Pull Requests

1. **Fork the repository** and create your branch from `main`
   ```bash
   git checkout -b feature/your-feature-name
   ```

2. **Make your changes**
   - Follow the existing code style
   - Add comments for complex logic
   - Update documentation as needed

3. **Test your changes**
   - Add tests for new functionality
   - Ensure all existing tests pass
   - Test with various input scenarios

4. **Commit your changes**
   - Use clear, descriptive commit messages
   - Follow the convention: `type: description`
   - Example: `feat: add support for multi-language extraction`

5. **Push to your fork** and submit a pull request
   ```bash
   git push origin feature/your-feature-name
   ```

## Development Setup

1. Clone your fork:
   ```bash
   git clone https://github.com/your-username/lazyFormFill.git
   cd lazyFormFill
   ```

2. Create a virtual environment:
   ```bash
   python -m venv .venv
   source .venv/bin/activate  # On Windows: .venv\Scripts\activate
   ```

3. Install dependencies:
   ```bash
   pip install -r requirements.txt
   python -m spacy download en_core_web_sm
   ```

4. Install development dependencies:
   ```bash
   pip install pytest jupyter
   ```

## Code Style Guidelines

- Follow PEP 8 style guidelines
- Use meaningful variable and function names
- Add docstrings to functions and classes
- Keep functions focused and modular
- Add type hints where appropriate

Example:
```python
def extract_birth_weight(text: str) -> float:
    """
    Extracts birth weight in kilograms from clinical text.
    
    Args:
        text (str): Clinical text containing birth weight information
        
    Returns:
        float: Birth weight in kg, or None if not found
    """
    # Implementation
    pass
```

## Testing Guidelines

- Write tests for new features
- Ensure tests are clear and well-documented
- Use descriptive test names
- Test edge cases and error conditions

Example test structure:
```python
def test_extract_birth_weight_with_kg():
    text = "Birth weight was 3.2 kg"
    result = extract_birth_weight(text)
    assert result == 3.2
```

## Documentation

- Update README.md if you add new features
- Add docstrings to new functions and classes
- Include usage examples for new functionality
- Update CHANGELOG.md with your changes

## Medical Data Handling

**Important**: When working with medical data:
- Never commit real patient data
- Use synthetic/anonymized data for testing
- Follow HIPAA and other relevant privacy regulations
- Be cautious with data handling in examples

## Questions?

If you have questions about contributing, feel free to:
- Open an issue for discussion
- Contact the maintainers

## Code of Conduct

- Be respectful and inclusive
- Welcome newcomers and help them contribute
- Focus on constructive feedback
- Assume good intentions

Thank you for contributing to LazyFormFill! 🎉
