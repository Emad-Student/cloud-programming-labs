# S1_MC_01.py
# Task: Day name using match/case (Python 3.10+)

def day_name(n: int):
    """
    Convert day number (1-7) to day name.
    Returns None for invalid input.
    """
    match n:
        case 1:
            return "Monday"
        case 2:
            return "Tuesday"
        case 3:
            return "Wednesday"
        case 4:
            return "Thursday"
        case 5:
            return "Friday"
        case 6:
            return "Saturday"
        case 7:
            return "Sunday"
        case _:
            return None

def main():
    print("Day Name Converter (using match/case):")
    print("=" * 40)
    
    # Test all valid days plus invalid cases
    test_cases = [1, 2, 3, 4, 5, 6, 7, 0, 8, -1, None]
    
    print(f"{'Input':<10} {'Day Name'}")
    print("-" * 40)
    
    for day_num in test_cases:
        result = day_name(day_num)
        result_str = result if result else "None (invalid)"
        print(f"{str(day_num):<10} {result_str}")
    
    print("=" * 40)

if __name__ == "__main__":
    main()
    