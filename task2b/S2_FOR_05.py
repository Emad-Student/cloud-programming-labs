# S2_FOR_05.py
# Task: Multiplication table 10×10

def print_multiplication_table():
    """
    Print a 10×10 multiplication table (1 to 10).
    Uses nested loops with aligned columns for readability.
    """
    print("10×10 Multiplication Table:")
    print("=" * 80)
    
    # Print header row
    print("    ", end="")
    for j in range(1, 11):
        print(f"{j:4}", end="")
    print()
    print("-" * 80)
    
    # Print each row
    for i in range(1, 11):
        print(f"{i:2} |", end="")
        for j in range(1, 11):
            product = i * j
            print(f"{product:4}", end="")
        print()
    
    print("=" * 80)

def main():
    print_multiplication_table()

if __name__ == "__main__":
    main()