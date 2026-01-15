# S1_VAR_08.py
# Task: Big integers (no MAX_SAFE_INTEGER problem)

def main():
    print("Testing big integers in Python:")
    print("=" * 60)
    
    # Compute a very large integer
    big_int = 10 ** 100
    print(f"big_int = 10 ** 100")
    print(f"Value: {big_int}")
    print(f"Type: {type(big_int).__name__}")
    print(f"Number of digits: {len(str(big_int))}")
    
    print("-" * 60)
    
    # Convert to float
    big_float = float(big_int)
    print(f"\nbig_float = float(10 ** 100)")
    print(f"Value: {big_float}")
    print(f"Type: {type(big_float).__name__}")
    
    print("-" * 60)
    
    # Show precision difference
    print("\nPrecision comparison:")
    small_int = 10 ** 20
    small_float = float(small_int)
    
    print(f"Integer: {small_int}")
    print(f"Float:   {small_float}")
    print(f"Equal? {small_int == small_float}")
    
    # Arithmetic with big integers
    result = big_int + 1
    print(f"\nbig_int + 1 has {len(str(result))} digits")
    print("Python maintains exact precision!")
    
    print("=" * 60)
    print("\nComment: Python integers have arbitrary precision.")
    print("Unlike JavaScript (MAX_SAFE_INTEGER = 2^53-1), Python")
    print("can handle integers of any size without loss of precision.")
    print("Floats still have limited precision (~15-17 decimal digits).")

if __name__ == "__main__":
    main()
    