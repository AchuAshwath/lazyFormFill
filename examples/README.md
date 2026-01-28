# Examples

This directory contains example scripts demonstrating how to use the LazyFormFill system.

## Available Examples

### 1. Basic Text Extraction (`basic_text_extraction.py`)

Demonstrates basic usage of the extraction system with simple clinical text.

**Run it:**
```bash
cd examples
python basic_text_extraction.py
```

**Features:**
- Single text extraction
- Processing multiple cases
- Display extracted fields

### 2. Dataset Processing (`dataset_processing.py`)

Shows how to process the included dataset and evaluate extraction accuracy.

**Run it:**
```bash
cd examples
python dataset_processing.py
```

**Features:**
- Process entire dataset
- Compare extracted vs expected results
- Calculate accuracy metrics
- Field-wise accuracy analysis

## Usage Tips

1. Make sure you have installed all dependencies before running examples:
   ```bash
   pip install -r requirements.txt
   python -m spacy download en_core_web_sm
   ```

2. Run examples from within the `examples` directory or adjust the Python path accordingly.

3. Modify the example scripts to test with your own data.

## Creating Your Own Examples

Feel free to create additional examples following this structure:

```python
import sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).parent.parent))

from main import extract_birth_history_from_dataset

# Your code here
text = "Your clinical text..."
result = extract_birth_history_from_dataset(text)
print(result)
```
