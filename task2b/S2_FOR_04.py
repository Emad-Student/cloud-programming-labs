# S2_FOR_04.py
# Task: Count occurrences (histogram)

def count_occurrences(values):
    """
    Count occurrences of each value in a list.
    Returns a dict with value → count.
    Manual implementation using a loop (no Counter).
    """
    counts = {}
    for value in values:
        if value in counts:
            counts[value] += 1
        else:
            counts[value] = 1
    return counts

def main():
    print("Count Occurrences Tests:")
    print("=" * 60)
    
    # Test cases
    test_cases = [
        ([1, 2, 2, 3, 3, 3], "Numbers"),
        (["a", "b", "a", "c", "b", "a"], "Strings"),
        ([1, 1, 1, 1], "All same"),
        ([], "Empty list"),
        ([1, 2, 3, 4, 5], "All unique"),
        (["red", "blue", "red", "green", "blue", "red"], "Colors"),
    ]
    
    for test_input, description in test_cases:
        result = count_occurrences(test_input)
        print(f"Input:  {test_input}")
        print(f"Result: {result}")
        print(f"Description: {description}")
        print("-" * 60)
    
    print("=" * 60)

if __name__ == "__main__":
    main()