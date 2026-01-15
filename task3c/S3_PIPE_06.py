# S3_PIPE_06.py
# Task: Safe pipeline (pipe_safe)

def pipe_safe(*fns):
    """
    Create a pipeline that catches exceptions.
    If any function raises, returns {"ok": False, "error": "..."}
    If all succeed, returns {"ok": True, "value": result}
    """
    def safe_piped(x):
        result = x
        try:
            for fn in fns:
                result = fn(result)
            return {"ok": True, "value": result}
        except Exception as e:
            return {"ok": False, "error": str(e)}
    return safe_piped

def main():
    print("Safe Pipeline Tests:")
    print("=" * 60)
    
    # Define some functions (one that can fail)
    add5 = lambda x: x + 5
    multiply2 = lambda x: x * 2
    divide_by = lambda divisor: lambda x: x / divisor
    must_be_positive = lambda x: x if x > 0 else (_ for _ in ()).throw(ValueError("Must be positive"))
    
    # Test 1: Successful pipeline
    print("Test 1: Successful pipeline")
    safe_transform = pipe_safe(add5, multiply2)
    result1 = safe_transform(10)
    print(f"  Input: 10")
    print(f"  Pipeline: add5 → multiply2")
    print(f"  Result: {result1}")
    print("-" * 60)
    
    # Test 2: Division by zero
    print("\nTest 2: Pipeline with division by zero")
    safe_divide = pipe_safe(add5, multiply2, divide_by(0))
    result2 = safe_divide(10)
    print(f"  Input: 10")
    print(f"  Pipeline: add5 → multiply2 → divide by 0")
    print(f"  Result: {result2}")
    print("-" * 60)
    
    # Test 3: Custom validation failure
    print("\nTest 3: Pipeline with validation failure")
    safe_validate = pipe_safe(lambda x: x - 20, must_be_positive, multiply2)
    result3 = safe_validate(10)
    print(f"  Input: 10")
    print(f"  Pipeline: subtract 20 → must_be_positive → multiply2")
    print(f"  Result: {result3}")
    print("-" * 60)
    
    # Test 4: Successful validation
    print("\nTest 4: Successful validation")
    result4 = safe_validate(30)
    print(f"  Input: 30")
    print(f"  Pipeline: subtract 20 → must_be_positive → multiply2")
    print(f"  Result: {result4}")
    
    print("=" * 60)
    print("\nKey feature: pipe_safe catches any exception and")
    print("returns a structured result instead of crashing.")

if __name__ == "__main__":
    main()