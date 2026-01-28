"""
Example: Dataset Processing

This example demonstrates how to process the included dataset and evaluate extraction accuracy.
"""

import sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).parent.parent))

from main import extract_birth_history_from_dataset
from data.dataset import Dataset

def process_dataset():
    """Process the entire dataset and display results."""
    
    print("=" * 80)
    print("Processing Birth History Dataset")
    print("=" * 80)
    print(f"\nTotal entries: {len(Dataset)}\n")
    
    total_fields = 0
    matched_fields = 0
    
    for idx, entry in enumerate(Dataset, 1):
        print(f"\n{'='*80}")
        print(f"Entry {idx}/{len(Dataset)}")
        print(f"{'='*80}")
        
        # Extract birth history
        extracted = extract_birth_history_from_dataset(entry['diagnosis_text'])
        expected = entry['expected_json']
        
        print("\nDiagnosis Text:")
        print("-" * 80)
        print(entry['diagnosis_text'][:200] + "..." if len(entry['diagnosis_text']) > 200 else entry['diagnosis_text'])
        
        print("\nComparison:")
        print("-" * 80)
        print(f"{'Field':<25} {'Expected':<20} {'Extracted':<20} {'Match':<10}")
        print("-" * 80)
        
        for field in expected.keys():
            exp_val = expected.get(field)
            ext_val = extracted.get(field)
            
            # Handle None values in comparison
            match = "✓" if ext_val == exp_val else "✗"
            
            total_fields += 1
            if ext_val == exp_val:
                matched_fields += 1
            
            print(f"{field:<25} {str(exp_val):<20} {str(ext_val):<20} {match:<10}")
    
    # Calculate overall accuracy
    accuracy = (matched_fields / total_fields * 100) if total_fields > 0 else 0
    
    print("\n" + "=" * 80)
    print(f"Overall Accuracy: {accuracy:.2f}%")
    print(f"Matched Fields: {matched_fields}/{total_fields}")
    print("=" * 80)
    
    return accuracy, matched_fields, total_fields


def analyze_field_accuracy():
    """Analyze accuracy for each field type."""
    
    print("\n" + "=" * 80)
    print("Field-wise Accuracy Analysis")
    print("=" * 80)
    
    field_stats = {}
    
    for entry in Dataset:
        extracted = extract_birth_history_from_dataset(entry['diagnosis_text'])
        expected = entry['expected_json']
        
        for field in expected.keys():
            if field not in field_stats:
                field_stats[field] = {'total': 0, 'correct': 0}
            
            field_stats[field]['total'] += 1
            if extracted.get(field) == expected.get(field):
                field_stats[field]['correct'] += 1
    
    print(f"\n{'Field':<25} {'Accuracy':<15} {'Correct/Total':<20}")
    print("-" * 80)
    
    for field, stats in sorted(field_stats.items()):
        accuracy = (stats['correct'] / stats['total'] * 100) if stats['total'] > 0 else 0
        print(f"{field:<25} {accuracy:>6.2f}%        {stats['correct']}/{stats['total']}")
    
    return field_stats


if __name__ == "__main__":
    # Process the full dataset
    accuracy, matched, total = process_dataset()
    
    # Analyze field-wise accuracy
    field_stats = analyze_field_accuracy()
    
    print("\n" + "=" * 80)
    print("Dataset Processing Complete!")
    print("=" * 80)
