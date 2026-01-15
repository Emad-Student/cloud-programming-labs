# S1_VAR_07.py
# Task: NaN and math.isnan

import math

def main():
    print("Testing NaN (Not a Number):")
    print("-" * 50)
    
    # Create NaN using float("nan")
    nan1 = float("nan")
    print(f"nan1 = float('nan'): {nan1}")
    
    # Try to create NaN using division by zero (will catch error)
    try:
        nan2 = 0.0 / 0.0
        print(f"nan2 = 0.0 / 0.0: {nan2}")
    except ZeroDivisionError as e:
        print(f"0.0 / 0.0 raised ZeroDivisionError: {e}")
        nan2 = float("nan")  # fallback
        print(f"Using fallback: nan2 = float('nan'): {nan2}")
    
    print("-" * 50)
    
    # Test NaN comparisons
    print("\nNaN comparison behavior:")
    print(f"nan1 == nan1: {nan1 == nan1}")
    print(f"nan1 == nan2: {nan1 == nan2}")
    print(f"nan1 is nan1: {nan1 is nan1}")
    print("Note: NaN is not equal to itself!")
    
    print("-" * 50)
    
    # Test math.isnan()
    print("\nUsing math.isnan() to detect NaN:")
    print(f"math.isnan(nan1): {math.isnan(nan1)}")
    print(f"math.isnan(nan2): {math.isnan(nan2)}")
    print(f"math.isnan(0.0): {math.isnan(0.0)}")
    print(f"math.isnan(42): {math.isnan(42)}")
    
    print("-" * 50)
    print("\nKey point: Use math.isnan() to check for NaN,")
    print("because NaN == NaN is always False!")

if __name__ == "__main__":
    main()
    