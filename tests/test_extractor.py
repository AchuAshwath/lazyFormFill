import time
from spacy_extractor import extract_radio_fields as pure_extract
from medspacy_extractor import extract_radio_fields_medspacy as med_extract

# Ground truth annotations for benchmarking
benchmark_cases = [
    {
        "text": "The baby was conceived naturally and delivered at term via NVD. He cried at birth.",
        "expected": {"conception_mode": "Natural", "delivery_mode": "NVD", "term": "Term", "cried_at_birth": "Yes"}
    },
    {
        "text": "This infant was conceived via IVF and delivered by caesarean section. The newborn did not cry.",
        "expected": {"conception_mode": "Assisted", "delivery_mode": "LSCS", "term": None, "cried_at_birth": "No"}
    },
    {
        "text": "A preterm male born by spontaneous vaginal delivery. Crying vigorously at birth.",
        "expected": {"conception_mode": None, "delivery_mode": "NVD", "term": "Preterm", "cried_at_birth": "Yes"}
    },
    {
        "text": "Premature birth at 35 weeks, no cry was noted. Delivery: assisted.",
        "expected": {"conception_mode": None, "delivery_mode": None, "term": "Preterm", "cried_at_birth": "No"}
    },
    {
        "text": "Infant conceived by ART, delivered normal vaginally at term, cried immediately.",
        "expected": {"conception_mode": "Assisted", "delivery_mode": "NVD", "term": "Term", "cried_at_birth": "Yes"}
    }
]

# Benchmark function
def evaluate(extractor, cases):
    correct = 0
    total = 0
    start = time.perf_counter()
    for case in cases:
        res = extractor(case["text"])
        for field, expected in case["expected"].items():
            total += 1
            if res.get(field) == expected:
                correct += 1
    elapsed = time.perf_counter() - start
    accuracy = correct / total * 100
    return accuracy, elapsed

if __name__ == "__main__":
    print("Benchmarking extraction accuracy and speed:\n")
    pure_acc, pure_time = evaluate(pure_extract, benchmark_cases)
    med_acc, med_time = evaluate(med_extract, benchmark_cases)

    print(f"Pure spaCy extractor -> Accuracy: {pure_acc:.2f}% | Time: {pure_time:.4f}s")
    print(f"medSpaCy-like extractor -> Accuracy: {med_acc:.2f}% | Time: {med_time:.4f}s")
    print("\nOverall: ")
    if pure_acc > med_acc:
        print("Pure spaCy is more accurate.")
    elif med_acc > pure_acc:
        print("medSpaCy-like is more accurate.")
    else:
        print("Both have equal accuracy.")
    if pure_time < med_time:
        print("Pure spaCy is faster.")
    else:
        print("medSpaCy-like is faster.")
