# S3_LAM_05.py
# Task: Higher-order predicate

def at_least(min_value):
    """
    Create a predicate function that checks if a value is >= min_value.
    Returns a lambda.
    """
    return lambda x: x >= min_value

def main():
    print("Higher-Order Predicate Tests:")
    print("=" * 60)
    
    # Test data
    numbers = [5, 12, 8, 3, 15, 20, 1, 9]
    
    print(f"Input numbers: {numbers}")
    print("-" * 60)
    
    # Create predicate: at least 10
    at_least_10 = at_least(10)
    
    # Use with filter
    result = list(filter(at_least_10, numbers))
    
    print(f"\nFilter with at_least(10):")
    print(f"  Result: {result}")
    print("-" * 60)
    
    # Another example: at least 15
    at_least_15 = at_least(15)
    result2 = list(filter(at_least_15, numbers))
    
    print(f"\nFilter with at_least(15):")
    print(f"  Result: {result2}")
    print("-" * 60)
    
    # Test individual values
    print(f"\nTesting at_least(10) on individual values:")
    for num in [5, 10, 15, 20]:
        passes = at_least_10(num)
        print(f"  {num} >= 10: {passes}")
    
    print("=" * 60)

if __name__ == "__main__":
    main()