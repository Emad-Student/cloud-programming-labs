# S1_IF_03.py
# Task: Normalize user name

def normalize_name(x):
    """
    Normalize a user name input.
    
    Rules:
    - If x is falsy → return "Anonymous"
    - Else return x.strip(), but if it becomes empty → "Anonymous"
    """
    if not x:
        return "Anonymous"
    
    normalized = x.strip()
    
    if not normalized:
        return "Anonymous"
    
    return normalized

def main():
    print("Name Normalization Tests:")
    print("=" * 50)
    
    # Test cases
    test_cases = [
        ("", "Empty string"),
        (" ", "Whitespace only"),
        (None, "None value"),
        (" Ola ", "Name with spaces"),
        ("John", "Normal name"),
        ("  ", "Multiple spaces"),
        ("   Alice   ", "Name with extra spaces"),
        (0, "Falsy number"),
        (False, "Boolean False"),
    ]
    
    print(f"{'Input':<20} {'Result':<20} {'Description'}")
    print("-" * 50)
    
    for test_input, description in test_cases:
        result = normalize_name(test_input)
        input_str = repr(test_input)[:18]
        print(f"{input_str:<20} {result:<20} {description}")
    
    print("=" * 50)

if __name__ == "__main__":
    main()
    