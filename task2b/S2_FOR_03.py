# S2_FOR_03.py
# Task: Sum until threshold

def sum_until(nums, threshold):
    """
    Sum numbers in order until adding the next would exceed threshold.
    Returns the final sum (without exceeding threshold).
    """
    total = 0
    for num in nums:
        if total + num > threshold:
            break
        total += num
    return total

def main():
    print("Sum Until Threshold Tests:")
    print("=" * 60)
    
    # Test cases
    test_cases = [
        ([1, 2, 3, 4, 5], 7, "Sum stops at 1+2+3=6"),
        ([10, 20, 30], 50, "Sum stops at 10+20=30"),
        ([5, 5, 5, 5], 20, "Exact match at 15"),
        ([100, 200], 50, "First element exceeds"),
        ([], 100, "Empty list"),
        ([1, 1, 1, 1, 1], 100, "All elements fit"),
    ]
    
    for nums, threshold, description in test_cases:
        result = sum_until(nums, threshold)
        print(f"Input:  nums={nums}, threshold={threshold}")
        print(f"Result: {result}")
        print(f"Description: {description}")
        print("-" * 60)
    
    print("=" * 60)

if __name__ == "__main__":
    main()
    