# S2_LIST_01.py
# Task: Clean number strings

def clean_numbers(values):
    """
    Convert a list of strings to floats, dropping invalid entries.
    - Trim each string
    - Convert to float
    - Drop items that fail conversion
    """
    result = []
    for value in values:
        try:
            trimmed = value.strip()
            number = float(trimmed)
            result.append(number)
        except (ValueError, AttributeError):
            # Skip invalid values
            pass
    return result

def main():
    print("Clean Number Strings Tests:")
    print("=" * 60)
    
    # Test cases
    test_cases = [
        ([" 1 ", "x", "2"], "Mixed valid and invalid"),
        (["3.14", " 2.71 ", "abc", "1.0"], "Floats with junk"),
        (["  10  ", "  20  ", "  30  "], "All valid with spaces"),
        (["", "  ", "x"], "All invalid"),
        (["100", "-50", "0"], "Integers as strings"),
    ]
    
    for test_input, description in test_cases:
        result = clean_numbers(test_input)
        print(f"Input:  {test_input}")
        print(f"Output: {result}")
        print(f"Description: {description}")
        print("-" * 60)
    
    print("=" * 60)

if __name__ == "__main__":
    main()