# S2_LIST_03.py
# Task: Chunk a list

def chunk(lst, size):
    """
    Split a list into chunks of given size.
    Last chunk may be shorter if list length is not divisible by size.
    Returns None if size <= 0.
    """
    if size <= 0:
        return None
    
    result = []
    for i in range(0, len(lst), size):
        result.append(lst[i:i + size])
    return result

def main():
    print("Chunk List Tests:")
    print("=" * 60)
    
    # Test cases
    test_cases = [
        ([1, 2, 3, 4, 5, 6, 7, 8], 3, "8 items, size 3"),
        ([1, 2, 3, 4, 5], 2, "5 items, size 2 (last chunk shorter)"),
        ([1, 2, 3, 4], 4, "Exact fit"),
        ([1, 2, 3], 5, "Size larger than list"),
        ([], 3, "Empty list"),
        ([1, 2, 3, 4, 5], 0, "Invalid size (0)"),
        ([1, 2, 3, 4, 5], -1, "Invalid size (negative)"),
    ]
    
    for test_list, size, description in test_cases:
        result = chunk(test_list, size)
        print(f"Input:  {test_list}, size={size}")
        print(f"Output: {result}")
        print(f"Description: {description}")
        print("-" * 60)
    
    print("=" * 60)

if __name__ == "__main__":
    main()
    