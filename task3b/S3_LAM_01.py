# S3_LAM_01.py
# Task: Convert to lambdas

def main():
    print("Lambda Function Tests:")
    print("=" * 60)
    
    # Define lambdas
    square = lambda n: n ** 2
    is_odd = lambda n: n % 2 != 0
    greet = lambda name: f"Hello, {name}!"
    
    # Test square
    print("Testing square(n):")
    print(f"  square(5) = {square(5)}")
    print(f"  square(10) = {square(10)}")
    print(f"  square(0) = {square(0)}")
    print("-" * 60)
    
    # Test is_odd
    print("\nTesting is_odd(n):")
    print(f"  is_odd(3) = {is_odd(3)}")
    print(f"  is_odd(4) = {is_odd(4)}")
    print(f"  is_odd(0) = {is_odd(0)}")
    print("-" * 60)
    
    # Test greet
    print("\nTesting greet(name):")
    print(f"  greet('Alice') = {greet('Alice')}")
    print(f"  greet('Bob') = {greet('Bob')}")
    print(f"  greet('Charlie') = {greet('Charlie')}")
    print("=" * 60)

if __name__ == "__main__":
    main()