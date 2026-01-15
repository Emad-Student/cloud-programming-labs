# S3_DICT_04.py
# Task: Omit keys

def omit(d, keys):
    """
    Create a new dict without the specified keys.
    """
    keys_to_omit = set(keys)
    return {k: v for k, v in d.items() if k not in keys_to_omit}

def main():
    print("Omit Keys Tests:")
    print("=" * 60)
    
    # Test data
    user = {
        "id": 1,
        "name": "Alice",
        "email": "alice@example.com",
        "password": "secret123",
        "role": "admin",
        "created_at": "2024-01-01"
    }
    
    # Test cases
    test_cases = [
        (["password"], "Remove sensitive field"),
        (["password", "created_at"], "Remove multiple fields"),
        (["invalid_key"], "Omit non-existent key (no effect)"),
        ([], "Omit nothing"),
        (["id", "password", "created_at"], "Remove several fields"),
    ]
    
    print("Original dict:")
    print(user)
    print("-" * 60)
    
    for keys_to_omit, description in test_cases:
        result = omit(user, keys_to_omit)
        print(f"\nOmit: {keys_to_omit}")
        print(f"Result: {result}")
        print(f"Description: {description}")
        print("-" * 60)
    
    print("=" * 60)

if __name__ == "__main__":
    main()
    