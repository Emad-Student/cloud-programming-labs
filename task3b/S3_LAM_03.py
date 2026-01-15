# S3_LAM_03.py
# Task: Closure factory

def make_adder(x):
    """
    Create a function that adds x to its input.
    Returns a lambda that captures x.
    """
    return lambda n: n + x

def main():
    print("Closure Factory Tests:")
    print("=" * 60)
    
    # Create adder functions
    add10 = make_adder(10)
    add3 = make_adder(3)
    
    # Test add10
    print("Testing add10 (adds 10):")
    print(f"  add10(5) = {add10(5)}")
    print(f"  add10(20) = {add10(20)}")
    print(f"  add10(0) = {add10(0)}")
    print("-" * 60)
    
    # Test add3
    print("\nTesting add3 (adds 3):")
    print(f"  add3(5) = {add3(5)}")
    print(f"  add3(20) = {add3(20)}")
    print(f"  add3(0) = {add3(0)}")
    print("-" * 60)
    
    # Show they're independent
    print("\nDemonstration that closures are independent:")
    print(f"  add10(1) = {add10(1)}")
    print(f"  add3(1) = {add3(1)}")
    print("  Each closure 'remembers' its own x value!")
    print("=" * 60)

if __name__ == "__main__":
    main()