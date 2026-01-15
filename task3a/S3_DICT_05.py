# S3_DICT_05.py
# Task: Invert with collisions

def invert(d):
    """
    Invert a dict: swap keys and values.
    If multiple keys have the same value, store a list of keys.
    """
    result = {}
    for key, value in d.items():
        if value in result:
            # Collision: convert to list if needed, then append
            if not isinstance(result[value], list):
                result[value] = [result[value]]
            result[value].append(key)
        else:
            result[value] = key
    return result

def main():
    print("Invert Dictionary Tests:")
    print("=" * 60)
    
    # Test cases
    test_cases = [
        ({"a": 1, "b": 2, "c": 3}, "No collisions"),
        ({"a": 1, "b": 1, "c": 2}, "Collision on value 1"),
        ({"x": "red", "y": "blue", "z": "red"}, "String values with collision"),
        ({"a": 1}, "Single entry"),
        ({}, "Empty dict"),
        ({"a": 1, "b": 1, "c": 1}, "All same value"),
    ]
    
    for test_dict, description in test_cases:
        result = invert(test_dict)
        print(f"Input:  {test_dict}")
        print(f"Output: {result}")
        print(f"Description: {description}")
        print("-" * 60)
    
    print("=" * 60)

if __name__ == "__main__":
    main()
    