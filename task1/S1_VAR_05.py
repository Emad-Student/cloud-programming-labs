# S1_VAR_05.py
# Task: Truthiness

def is_truthy(v):
    """Returns the truthiness of a value using bool()"""
    return bool(v)

def main():
    print("Testing truthiness:")
    print("-" * 50)
    
    # Test values
    test_values = [
        0,
        1,
        "",
        "0",
        [],
        [0],
        {},
        None
    ]
    
    # Print results in table format
    print(f"{'Value':<15} {'Type':<15} {'Truthy?'}")
    print("-" * 50)
    
    for val in test_values:
        val_str = repr(val)[:13]
        type_name = type(val).__name__
        truthy = is_truthy(val)
        print(f"{val_str:<15} {type_name:<15} {truthy}")
    
    print("-" * 50)
    print("\nKey observations:")
    print("- 0, empty strings, empty lists, empty dicts, and None are falsy")
    print("- Non-zero numbers, non-empty collections are truthy")
    print("- String '0' is truthy (non-empty string)")

if __name__ == "__main__":
    main()