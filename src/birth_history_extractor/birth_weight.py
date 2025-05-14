import re

try:
    from word2number import w2n
except ImportError:
    w2n = None


def extract_birth_weight(text: str) -> float:
    """
    Extracts birth weight in kilograms from a clinical text.
    Returns the weight in kg, or None if no weight is found.
    """
    # Numeric pattern for kg or g
    numeric_match = re.search(
        r'(\d+(?:[\d,]*)(?:\.\d+)?)\s*(kg|kilograms|g|grams|kilos)',
        text,
        re.IGNORECASE
    )
    if numeric_match:
        # print(f"Numeric match: {numeric_match.group(0)}")
        value = float(numeric_match.group(1).replace(',', ''))
        unit = numeric_match.group(2).lower()
        if unit in ['g', 'grams']:
            # print(f"Unit: {unit}")
            value = value / 1000
        return value

    # Spelled-out number pattern for kg/kilos
    if w2n:
        # print("Word2Number is available")
        spelled_match = re.search(
            r'([a-z\s\-\d]+?)\s*(kg|kilograms|kilos)',
            text,
            re.IGNORECASE
        )
        if spelled_match:
            # print(f"Spelled match: {spelled_match.group(0)}")
            words = spelled_match.group(1)
            try:
                num = w2n.word_to_num(words)
                return float(num)
            except Exception:
                pass

    return None
