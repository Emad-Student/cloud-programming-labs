# S1_VAR_09.py
# Task: Type hints are not runtime enforcement

def add(a: int, b: int) -> int:
    """
    Add two integers.
    Type hints suggest integers, but Python doesn't enforce this at runtime.
    """
    return a + b

def main():
    print("Testing type hints:")
    print("-" * 50)
    
    # Correct usage with integers
    result1 = add(5, 3)
    print(f"add(5, 3) = {result1}")
    print(f"Type of result: {type(result1).__name__}")
    
    print("-" * 50)
    
    # "Incorrect" usage with strings (but it still works!)
    result2 = add("Hello ", "World")
    print(f"add('Hello ', 'World') = {result2}")
    print(f"Type of result: {type(result2).__name__}")
    
    print("-" * 50)
    
    # Another example with floats
    result3 = add(3.5, 2.7)
    print(f"add(3.5, 2.7) = {result3}")
    print(f"Type of result: {type(result3).__name__}")
    
    print("=" * 50)
    print("\nComment: Type hints are for tooling and readability,")
    print("NOT automatic runtime checks. Python doesn't enforce them.")
    print("Static type checkers (like mypy) can catch these issues")
    print("during development, but the code will still run at runtime.")

if __name__ == "__main__":
    main()
    