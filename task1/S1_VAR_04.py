# S1_VAR_04.py
# Task: Identity vs equality (is vs ==)

def main():
    print("Identity (is) vs Equality (==):")
    print("-" * 50)
    
    # Example 1: Small integers (Python caches these)
    a = 256
    b = 256
    print(f"a = {a}, b = {b}")
    print(f"a == b: {a == b}")
    print(f"a is b: {a is b}")
    print()
    
    # Example 2: Larger integers (not cached)
    x = 1000
    y = 1000
    print(f"x = {x}, y = {y}")
    print(f"x == y: {x == y}")
    print(f"x is y: {x is y}")
    print()
    
    # Example 3: Lists with same content
    list1 = [1, 2, 3]
    list2 = [1, 2, 3]
    print(f"list1 = {list1}, list2 = {list2}")
    print(f"list1 == list2: {list1 == list2}")
    print(f"list1 is list2: {list1 is list2}")
    print()
    
    # Example 4: Correct use of 'is' with None
    value = None
    print(f"value = {value}")
    print(f"value is None: {value is None}")
    print(f"value == None: {value == None} (works but 'is' is preferred)")
    
    print("-" * 50)
    print("\nComment: Use 'is' for identity (same object in memory),")
    print("use '==' for equality (same value).")

if __name__ == "__main__":
    main()
    