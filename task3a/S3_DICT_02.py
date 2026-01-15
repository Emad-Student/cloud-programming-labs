# S3_DICT_02.py
# Task: Merge defaults (shallow)

def merge_defaults(defaults, overrides):
    """
    Merge two dicts: defaults provides base values, overrides wins for conflicts.
    Returns a new dict (shallow merge).
    Uses dict unpacking syntax.
    """
    return {**defaults, **overrides}

def main():
    print("Merge Defaults Tests:")
    print("=" * 60)
    
    # Test 1: Basic merge
    defaults = {"theme": "light", "lang": "en", "size": "medium"}
    overrides = {"theme": "dark", "size": "large"}
    result = merge_defaults(defaults, overrides)
    
    print("Test 1: Basic merge")
    print(f"Defaults:  {defaults}")
    print(f"Overrides: {overrides}")
    print(f"Result:    {result}")
    print("-" * 60)
    
    # Test 2: Empty overrides
    result2 = merge_defaults(defaults, {})
    print("\nTest 2: Empty overrides")
    print(f"Result: {result2}")
    print("-" * 60)
    
    # Test 3: Shallow merge demonstration
    defaults_nested = {"config": {"a": 1, "b": 2}, "name": "app"}
    overrides_nested = {"config": {"c": 3}}
    result3 = merge_defaults(defaults_nested, overrides_nested)
    
    print("\nTest 3: Shallow merge (nested dict replaced, not merged)")
    print(f"Defaults:  {defaults_nested}")
    print(f"Overrides: {overrides_nested}")
    print(f"Result:    {result3}")
    print("Note: The entire 'config' dict was replaced, not merged.")
    print("This is shallow merge - nested objects are NOT merged recursively.")
    print("=" * 60)

if __name__ == "__main__":
    main()