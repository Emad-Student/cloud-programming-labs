# S2_LIST_02.py
# Task: Deduplicate without set

def unique(values):
    """
    Remove duplicates from a list, preserving first occurrence order.
    Does not use set() - implements manually for practice.
    """
    result = []
    for value in values:
        if value not in result:
            result.append(value)
    return result

def main():
    print("Deduplication Tests (without using set):")
    print("=" * 60)
    
    # Test cases
    test_cases = [
        ([1, 2, 3, 2, 1, 4], "Integers with duplicates"),
        (["a", "b", "a", "c", "b"], "Strings with duplicates"),
        ([1, 1, 1, 1], "All same values"),
        ([1, 2, 3, 4, 5], "No duplicates"),
        ([], "Empty list"),
        ([5, 3, 5, 1, 3, 5], "Multiple occurrences"),
    ]
    
    for test_input, description in test_cases:
        result = unique(test_input)
        print(f"Input:  {test_input}")
        print(f"Output: {result}")
        print(f"Description: {description}")
        print("-" * 60)
    
    print("=" * 60)

if __name__ == "__main__":
    main()
    