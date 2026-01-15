# S3_PIPE_02.py
# Task: Implement compose(*fns)

def compose(*fns):
    """
    Create a function that applies functions right-to-left.
    compose(f, g, h)(x) == f(g(h(x)))
    """
    def composed(x):
        result = x
        for fn in reversed(fns):
            result = fn(result)
        return result
    return composed

def pipe(*fns):
    """pipe applies left-to-right (for comparison)"""
    def piped(x):
        result = x
        for fn in fns:
            result = fn(result)
        return result
    return piped

def main():
    print("Compose vs Pipe Comparison:")
    print("=" * 60)
    
    # Define transformations
    add5 = lambda x: x + 5
    multiply2 = lambda x: x * 2
    subtract3 = lambda x: x - 3
    
    # Create pipelines
    piped = pipe(add5, multiply2, subtract3)
    composed = compose(add5, multiply2, subtract3)
    
    # Test value
    test_val = 10
    
    print(f"Input: {test_val}")
    print(f"Functions: add5, multiply2, subtract3")
    print("-" * 60)
    
    # Pipe (left-to-right)
    pipe_result = piped(test_val)
    print(f"\nPipe (left-to-right):")
    print(f"  {test_val} → add5 → multiply2 → subtract3")
    print(f"  {test_val} → {test_val + 5} → {(test_val + 5) * 2} → {((test_val + 5) * 2) - 3}")
    print(f"  Result: {pipe_result}")
    
    # Compose (right-to-left)
    compose_result = composed(test_val)
    print(f"\nCompose (right-to-left):")
    print(f"  {test_val} → subtract3 → multiply2 → add5")
    print(f"  {test_val} → {test_val - 3} → {(test_val - 3) * 2} → {((test_val - 3) * 2) + 5}")
    print(f"  Result: {compose_result}")
    
    print("=" * 60)
    print("\nKey difference:")
    print("  pipe(f, g, h) applies functions left-to-right: h(g(f(x)))")
    print("  compose(f, g, h) applies functions right-to-left: f(g(h(x)))")

if __name__ == "__main__":
    main()