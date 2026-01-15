# S3_LAM_04.py
# Task: Sum of squares of even numbers

from functools import reduce

def sum_of_squares_of_evens(nums):
    """
    Calculate sum of squares of even numbers.
    Uses filter, map, and reduce.
    """
    # Filter even numbers
    evens = filter(lambda n: n % 2 == 0, nums)
    evens_list = list(evens)
    print(f"  Even numbers: {evens_list}")
    
    # Square them
    squares = map(lambda n: n ** 2, evens_list)
    squares_list = list(squares)
    print(f"  Squares: {squares_list}")
    
    # Sum them
    total = reduce(lambda a, b: a + b, squares_list, 0)
    print(f"  Sum: {total}")
    
    return total

def main():
    print("Sum of Squares of Even Numbers:")
    print("=" * 60)
    
    # Test cases
    test_cases = [
        [1, 2, 3, 4, 5, 6],
        [10, 15, 20, 25],
        [1, 3, 5, 7],
        [2, 4, 6, 8],
    ]
    
    for nums in test_cases:
        print(f"\nInput: {nums}")
        result = sum_of_squares_of_evens(nums)
        print(f"Final result: {result}")
        print("-" * 60)
    
    print("=" * 60)

if __name__ == "__main__":
    main()
    