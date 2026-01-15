# S2_FOR_02.py
# Task: Find first even

def find_first_even(nums):
    """
    Find and return the first even number in a list.
    Returns None if no even number is found.
    Uses a loop (not next() with generator).
    """
    for num in nums:
        if num % 2 == 0:
            return num
    return None

def main():
    print("Find First Even Tests:")
    print("=" * 60)
    
    # Test cases
    test_cases = [
        ([1, 3, 5, 7, 8, 9], "Even in middle"),
        ([2, 4, 6], "All even"),
        ([1, 3, 5], "No even"),
        ([1, 3, 4, 6, 8], "Multiple evens"),
        ([], "Empty list"),
        ([10], "Single even"),
        ([7], "Single odd"),
    ]
    
    for test_input, description in test_cases:
        result = find_first_even(test_input)
        print(f"Input:  {test_input}")
        print(f"Result: {result}")
        print(f"Description: {description}")
        print("-" * 60)
    
    print("=" * 60)

if __name__ == "__main__":
    main()
    