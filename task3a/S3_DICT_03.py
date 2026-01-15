# S3_DICT_03.py
# Task: Pick keys

def pick(d, keys):
    """
    Create a new dict with only the specified keys (if they exist).
    """
    return {k: d[k] for k in keys if k in d}

def main():
    print("Pick Keys Tests:")
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
        (["id", "name", "email"], "Pick public fields"),
        (["name"], "Pick single field"),
        (["id", "name", "invalid_key"], "Include non-existent key"),
        ([], "Pick no keys"),
        (["password", "role"], "Pick sensitive fields"),
    ]
    
    print("Original dict:")
    print(user)
    print("-" * 60)
    
    for keys_to_pick, description in test_cases:
        result = pick(user, keys_to_pick)
        print(f"\nKeys: {keys_to_pick}")
        print(f"Result: {result}")
        print(f"Description: {description}")
        print("-" * 60)
    
    print("=" * 60)

if __name__ == "__main__":
    main()
    