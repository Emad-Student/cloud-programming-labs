# S2_FOR_06.py
# Task: Sum nested lists (matrix)

def sum_nested(matrix):
    """
    Sum all numbers in a matrix (list of lists).
    Validates each row is a list; returns None if validation fails.
    """
    # Validate that matrix is a list
    if not isinstance(matrix, list):
        return None
    
    total = 0
    for row in matrix:
        # Validate that each row is a list
        if not isinstance(row, list):
            return None
        
        # Sum the row
        for value in row:
            total += value
    
    return total

def main():
    print("Sum Nested Lists (Matrix) Tests:")
    print("=" * 60)
    
    # Test cases
    test_cases = [
        ([[1, 2, 3], [4, 5, 6]], "2×3 matrix"),
        ([[10], [20], [30]], "Column vector"),
        ([[1, 2, 3, 4, 5]], "Row vector"),
        ([[], [], []], "Empty rows"),
        ([[]], "Single empty row"),
        ([[1, 2], [3, 4], [5, 6, 7]], "Irregular matrix"),
        ([1, 2, 3], "Invalid: not nested (should fail)"),
    ]
    
    for test_input, description in test_cases:
        result = sum_nested(test_input)
        print(f"Input:  {test_input}")
        print(f"Result: {result}")
        print(f"Description: {description}")
        print("-" * 60)
    
    print("=" * 60)

if __name__ == "__main__":
    main()
    