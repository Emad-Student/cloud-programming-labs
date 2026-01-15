# S3_DICT_01.py
# Task: Safe get by dotted path

def get_path(obj, path, fallback):
    """
    Safely navigate a nested dict using a dotted path like "a.b.c".
    Returns fallback if any step is missing or not a dict.
    """
    keys = path.split(".")
    current = obj
    
    for key in keys:
        if not isinstance(current, dict):
            return fallback
        if key not in current:
            return fallback
        current = current[key]
    
    return current

def main():
    print("Safe Get Path Tests:")
    print("=" * 60)
    
    # Test data
    data = {
        "user": {
            "name": "Alice",
            "address": {
                "city": "Warsaw",
                "country": "Poland"
            },
            "age": 30
        },
        "status": "active"
    }
    
    # Test cases
    test_cases = [
        ("user.name", "N/A", "Valid path"),
        ("user.address.city", "N/A", "Nested path"),
        ("user.address.zip", "00-000", "Missing key"),
        ("user.phone.number", "N/A", "Path through missing key"),
        ("status", "unknown", "Top-level key"),
        ("invalid.path", "default", "Completely invalid"),
        ("user.age", 0, "Number value"),
    ]
    
    print("Test data:")
    print(data)
    print("-" * 60)
    
    for path, fallback, description in test_cases:
        result = get_path(data, path, fallback)
        print(f"Path: '{path}'")
        print(f"Result: {result}")
        print(f"Description: {description}")
        print("-" * 60)
    
    print("=" * 60)

if __name__ == "__main__":
    main()
    