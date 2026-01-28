"""
Example: Basic Text Extraction

This example demonstrates how to extract birth history information from clinical text.
"""

# Add the parent directory to the path to import from src
import sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).parent.parent))

from main import extract_birth_history_from_dataset

def example_basic_extraction():
    """Example of basic birth history extraction from text."""
    
    # Sample clinical text
    clinical_text = """
    A 4-year-old child with a family history of diabetes. 
    The child was conceived naturally and delivered by caesarean section at 38 weeks. 
    The baby cried immediately after birth. Birth weight was 3.2 kg.
    There were no postnatal complications, and breastfeeding continued for 4 months.
    """
    
    print("Clinical Text:")
    print("-" * 80)
    print(clinical_text)
    print("\n")
    
    # Extract birth history
    birth_history = extract_birth_history_from_dataset(clinical_text)
    
    print("Extracted Birth History:")
    print("-" * 80)
    for field, value in birth_history.items():
        print(f"{field:25s}: {value}")
    
    return birth_history


def example_multiple_cases():
    """Example of processing multiple clinical texts."""
    
    cases = [
        {
            "patient_id": "P001",
            "text": "Baby born preterm at 32 weeks via NVD. Cried immediately. Birth weight 2.5 kg."
        },
        {
            "patient_id": "P002", 
            "text": "Full term delivery by caesarean section. Conceived through IVF. Baby weight 3.4 kg."
        },
        {
            "patient_id": "P003",
            "text": "Natural conception, normal vaginal delivery at 39 weeks. Baby cried vigorously at birth."
        }
    ]
    
    results = []
    
    print("\nProcessing Multiple Cases:")
    print("=" * 80)
    
    for case in cases:
        print(f"\nPatient ID: {case['patient_id']}")
        print(f"Text: {case['text']}")
        
        birth_history = extract_birth_history_from_dataset(case['text'])
        
        print("Extracted Data:")
        for field, value in birth_history.items():
            if value is not None:
                print(f"  {field}: {value}")
        
        results.append({
            "patient_id": case['patient_id'],
            "extracted_data": birth_history
        })
        
        print("-" * 80)
    
    return results


if __name__ == "__main__":
    print("=" * 80)
    print("LazyFormFill - Basic Text Extraction Examples")
    print("=" * 80)
    print()
    
    # Run basic extraction example
    example_basic_extraction()
    
    print("\n" + "=" * 80 + "\n")
    
    # Run multiple cases example
    example_multiple_cases()
