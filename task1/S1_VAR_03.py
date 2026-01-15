# S1_VAR_03.py
# Task: Mutability: list vs tuple

def main():
    print("Testing mutability:")
    print("-" * 50)
    
    # Lists are mutable
    lst = [1, 2, 3]
    print(f"Original list: {lst}")
    lst[1] = 99
    print(f"Modified list: {lst}")
    print("✓ List modification succeeded - lists are mutable")
    
    print("-" * 50)
    
    # Tuples are immutable
    tup = (1, 2, 3)
    print(f"Original tuple: {tup}")
    
    try:
        tup[1] = 99
        print("✗ Tuple modification succeeded (shouldn't happen!)")
    except TypeError as e:
        print(f"✓ Tuple modification failed with error: {e}")
        print("This is expected - tuples are immutable")
    
    print("-" * 50)
    print("\nExplanation:")
    print("Lists are mutable - you can change their elements after creation.")
    print("Tuples are immutable - once created, their elements cannot be changed.")

if __name__ == "__main__":
    main()
    