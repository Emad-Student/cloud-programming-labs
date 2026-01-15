# S1_VAR_10.py
# Task: Mini inspector

def inspect(v):
    """
    Returns a dict with information about a value:
    - type_name: the name of the type
    - is_none: whether the value is None
    - is_callable: whether the value can be called
    - is_iterable: whether the value can be iterated over
    - truthy: the truthiness of the value
    """
    # Check if iterable
    try:
        iter(v)
        iterable = True
    except TypeError:
        iterable = False
    
    return {
        "type_name": type(v).__name__,
        "is_none": v is None,
        "is_callable": callable(v),
        "is_iterable": iterable,
        "truthy": bool(v)
    }

def main():
    print("Mini Inspector Results:")
    print("=" * 80)
    
    # Test values
    test_values = [
        42,
        0,
        3.14,
        "hello",
        "",
        True,
        False,
        None,
        [1, 2, 3],
        [],
        {"key": "value"},
        lambda x: x * 2,
        print,
        range(5)
    ]
    
    # Print header
    print(f"{'Value':<15} {'type_name':<12} {'is_none':<8} {'callable':<9} {'iterable':<9} {'truthy'}")
    print("-" * 80)
    
    # Inspect each value
    for val in test_values:
        result = inspect(val)
        val_str = repr(val)[:13]
        print(f"{val_str:<15} {result['type_name']:<12} {str(result['is_none']):<8} "
              f"{str(result['is_callable']):<9} {str(result['is_iterable']):<9} {result['truthy']}")
    
    print("=" * 80)

if __name__ == "__main__":
    main()
    
    