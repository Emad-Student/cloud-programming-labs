# S1_VAR_02.py
# Task: Rebinding and dynamic typing

def main():
    print("Demonstrating dynamic typing:")
    print("-" * 50)
    
    # Assign different types to the same variable name
    x = 42
    print(f"x = {x}, type: {type(x).__name__}")
    
    x = "hello"
    print(f"x = {x}, type: {type(x).__name__}")
    
    x = [1, 2, 3]
    print(f"x = {x}, type: {type(x).__name__}")
    
    x = 3.14
    print(f"x = {x}, type: {type(x).__name__}")
    
    print("-" * 50)
    print("\nComment about dynamic typing:")
    print("Dynamic typing means that variables in Python don't have")
    print("a fixed type. The same variable name can hold values of")
    print("different types at different times during execution.")

if __name__ == "__main__":
    main()