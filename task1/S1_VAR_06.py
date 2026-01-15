# S1_VAR_06.py
# Task: Safe conversion: int() / float()

def to_int_or_none(s):
    """
    Safely convert a value to int, returning None on failure.
    Handles None input safely.
    """
    if s is None:
        return None
    
    try:
        return int(s)
    except (ValueError, TypeError):
        return None

def main():
    print("Testing safe int conversion:")
    print("-" * 50)
    
    # Test cases
    test_cases = ["12", " 12 ", "12x", "", None]
    
    print(f"{'Input':<15} {'Result':<15} {'Type'}")
    print("-" * 50)
    
    for test in test_cases:
        result = to_int_or_none(test)
        input_str = repr(test)[:13]
        result_str = str(result)
        result_type = type(result).__name__ if result is not None else "NoneType"
        print(f"{input_str:<15} {result_str:<15} {result_type}")
    
    print("-" * 50)
    print("\nObservations:")
    print("- Valid integer strings convert successfully")
    print("- Strings with spaces get trimmed by int()")
    print("- Invalid strings return None")
    print("- Empty strings and None return None")

if __name__ == "__main__":
    main()