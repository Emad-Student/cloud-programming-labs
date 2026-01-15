# S2_LIST_05.py
# Task: Stats

def stats(nums):
    """
    Calculate statistics for a list of numbers.
    Returns dict with: min, max, avg, sum
    Returns None for empty list.
    """
    if not nums:
        return None
    
    total = sum(nums)
    count = len(nums)
    
    return {
        "min": min(nums),
        "max": max(nums),
        "avg": total / count,
        "sum": total
    }

def main():
    print("Statistics Tests:")
    print("=" * 60)
    
    # Test cases
    test_cases = [
        ([1, 2, 3, 4, 5], "Positive integers"),
        ([-5, -2, 0, 3, 7], "Mixed positive and negative"),
        ([100], "Single value"),
        ([10, 10, 10, 10], "All same values"),
        ([], "Empty list"),
        ([-10, -20, -30], "All negative"),
        ([1.5, 2.5, 3.5], "Floats"),
    ]
    
    for test_input, description in test_cases:
        result = stats(test_input)
        print(f"Input: {test_input}")
        print(f"Description: {description}")
        if result:
            print(f"  Min: {result['min']}")
            print(f"  Max: {result['max']}")
            print(f"  Avg: {result['avg']}")
            print(f"  Sum: {result['sum']}")
        else:
            print(f"  Result: None (empty list)")
        print("-" * 60)
    
    print("=" * 60)

if __name__ == "__main__":
    main()