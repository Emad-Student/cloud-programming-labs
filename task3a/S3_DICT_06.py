# S3_DICT_06.py
# Task: Group by property

def group_by(items, key):
    """
    Group a list of dicts by a property.
    Returns dict: property_value → list of items with that value.
    """
    result = {}
    for item in items:
        value = item.get(key)
        if value not in result:
            result[value] = []
        result[value].append(item)
    return result

def main():
    print("Group By Property Tests:")
    print("=" * 60)
    
    # Test data
    users = [
        {"name": "Alice", "role": "admin", "age": 30},
        {"name": "Bob", "role": "user", "age": 25},
        {"name": "Charlie", "role": "admin", "age": 35},
        {"name": "Diana", "role": "user", "age": 28},
        {"name": "Eve", "role": "moderator", "age": 30},
    ]
    
    print("Test data:")
    for user in users:
        print(f"  {user}")
    print("-" * 60)
    
    # Group by role
    print("\nGroup by 'role':")
    by_role = group_by(users, "role")
    for role, group in by_role.items():
        print(f"  {role}: {[u['name'] for u in group]}")
    print("-" * 60)
    
    # Group by age
    print("\nGroup by 'age':")
    by_age = group_by(users, "age")
    for age, group in by_age.items():
        print(f"  {age}: {[u['name'] for u in group]}")
    print("-" * 60)
    
    # Group by non-existent key
    print("\nGroup by 'department' (non-existent key):")
    by_dept = group_by(users, "department")
    print(f"  Result: {by_dept}")
    print("=" * 60)

if __name__ == "__main__":
    main()
    