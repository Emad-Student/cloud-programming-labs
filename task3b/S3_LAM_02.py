# S3_LAM_02.py
# Task: Sort by key

def main():
    print("Sort by Key Tests:")
    print("=" * 60)
    
    # Test data
    people = [
        {"name": "Charlie", "age": 35},
        {"name": "Alice", "age": 30},
        {"name": "Bob", "age": 25},
        {"name": "Diana", "age": 28},
    ]
    
    print("Before sorting:")
    for person in people:
        print(f"  {person}")
    print("-" * 60)
    
    # Sort by age ascending
    sorted_people = sorted(people, key=lambda p: p["age"])
    
    print("\nAfter sorting by age (ascending):")
    for person in sorted_people:
        print(f"  {person}")
    print("-" * 60)
    
    # Bonus: Sort by name
    sorted_by_name = sorted(people, key=lambda p: p["name"])
    
    print("\nBonus - Sorted by name (ascending):")
    for person in sorted_by_name:
        print(f"  {person}")
    print("=" * 60)

if __name__ == "__main__":
    main()
    