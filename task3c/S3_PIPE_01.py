# S3_PIPE_01.py
# Task: Implement pipe(*fns)

def pipe(*fns):
    """
    Create a function that applies functions left-to-right.
    pipe(f, g, h)(x) == h(g(f(x)))
    """
    def piped(x):
        result = x
        for fn in fns:
            result = fn(result)
        return result
    return piped

def main():
    print("Pipe Function Tests:")
    print("=" * 60)
    
    # Define some simple transformations
    add5 = lambda x: x + 5
    multiply2 = lambda x: x * 2
    subtract3 = lambda x: x - 3
    
    # Create a pipeline
    transform = pipe(add5, multiply2, subtract3)
    
    # Test cases
    print("Pipeline: add5 → multiply2 → subtract3")
    print("-" * 60)
    
    test_values = [0, 5, 10, -3]
    
    for val in test_values:
        result = transform(val)
        # Show step-by-step
        step1 = add5(val)
        step2 = multiply2(step1)
        step3 = subtract3(step2)
        print(f"Input: {val}")
        print(f"  After add5: {step1}")
        print(f"  After multiply2: {step2}")
        print(f"  After subtract3: {step3}")
        print(f"  Final result: {result}")
        print("-" * 60)
    
    print("=" * 60)

if __name__ == "__main__":
    main()
    