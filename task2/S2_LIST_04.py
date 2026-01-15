# S2_LIST_04.py
# Task: Flatten one level

def flatten1(lst):
    """
    Flatten a list by one level.
    Elements can be items or lists of items.
    Does NOT recursively flatten (only one level).
    Manual implementation (no itertools.chain.from_iterable).
    """
    result = []
    for item in lst:
        if isinstance(item, list):
            # It's a list, extend result with its items
            result.extend(item)
        else:
            # It's a single item, append it
            result.append(item)
    return result

def main():
    print("Flatten One Level Tests:")
    print("=" * 60)
    
    # Test cases
    test_cases = [
        ([1, [2, 3], 4], "Mix of items and lists"),
        ([[1, 2], [3, 4], [5]], "All lists"),
        ([1, 2, 3], "No nested lists"),
        ([[], [1], [], [2, 3]], "Empty lists mixed in"),
        ([[1, [2, 3]], 4], "Nested list (only flattens 1 level)"),
        ([], "Empty list"),
    ]
    
    for test_input, description in test_cases:
        result = flatten1(test_input)
        print(f"Input:  {test_input}")
        print(f"Output: {result}")
        print(f"Description: {description}")
        print("-" * 60)
    
    print("=" * 60)

if __name__ == "__main__":
    main()