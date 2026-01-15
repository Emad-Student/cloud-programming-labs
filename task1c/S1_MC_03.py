# S1_MC_03.py
# Task: Simple calculator using match/case

def calc(a, op, b):
    """
    Perform basic arithmetic operations.
    
    Args:
        a: first number
        op: operator ("+", "-", "*", "/")
        b: second number
    
    Returns:
        Result of the operation, or None for invalid inputs/division by zero
    """
    # Validate inputs are numbers
    try:
        num_a = float(a)
        num_b = float(b)
    except (ValueError, TypeError):
        return None
    
    # Perform operation using match
    match op:
        case "+":
            return num_a + num_b
        case "-":
            return num_a - num_b
        case "*":
            return num_a * num_b
        case "/":
            if num_b == 0:
                return None  # Division by zero
            return num_a / num_b
        case _:
            return None  # Unknown operator

def main():
    print("Calculator Tests:")
    print("=" * 50)
    
    # Test cases (a, op, b, description)
    tests = [
        (10, "+", 5, "Addition"),
        (10, "-", 5, "Subtraction"),
        (10, "*", 5, "Multiplication"),
        (10, "/", 5, "Division"),
        (10, "/", 0, "Division by zero"),
        (10, "%", 5, "Invalid operator"),
        ("abc", "+", 5, "Invalid first operand"),
        (10, "+", "xyz", "Invalid second operand"),
        (7, "+", 3, "Another addition"),
        (100, "/", 4, "Another division"),
    ]
    
    print(f"{'Expression':<20} {'Result':<15} {'Description'}")
    print("-" * 50)
    
    for a, op, b, desc in tests:
        result = calc(a, op, b)
        expr = f"{a} {op} {b}"
        result_str = str(result) if result is not None else "None (error)"
        print(f"{expr:<20} {result_str:<15} {desc}")
    
    print("=" * 50)

if __name__ == "__main__":
    main()
    