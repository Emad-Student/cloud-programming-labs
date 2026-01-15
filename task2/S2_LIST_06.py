# S2_LIST_06.py
# Task: Transform records

def get_active_user_names(users):
    """
    From a list of user dicts, return names of active users,
    uppercased and sorted A→Z.
    Uses list comprehension + sorted().
    """
    # Filter active users, extract names, uppercase, then sort
    return sorted([user["name"].upper() for user in users if user.get("active", False)])

def main():
    print("Transform Records Tests:")
    print("=" * 60)
    
    # Test data
    users = [
        {"id": 1, "name": "Alice", "active": True},
        {"id": 2, "name": "Bob", "active": False},
        {"id": 3, "name": "Charlie", "active": True},
        {"id": 4, "name": "Diana", "active": True},
        {"id": 5, "name": "Eve", "active": False},
        {"id": 6, "name": "frank", "active": True},
    ]
    
    print("Input users:")
    for user in users:
        status = "active" if user["active"] else "inactive"
        print(f"  {user['id']}: {user['name']} ({status})")
    
    print("-" * 60)
    
    result = get_active_user_names(users)
    
    print(f"\nActive users (uppercased, sorted):")
    print(f"  {result}")
    
    print("-" * 60)
    
    # Additional test: empty list
    print("\nTest with empty list:")
    result2 = get_active_user_names([])
    print(f"  Result: {result2}")
    
    # Additional test: no active users
    print("\nTest with no active users:")
    inactive_users = [
        {"id": 1, "name": "John", "active": False},
        {"id": 2, "name": "Jane", "active": False},
    ]
    result3 = get_active_user_names(inactive_users)
    print(f"  Result: {result3}")
    
    print("=" * 60)

if __name__ == "__main__":
    main()
    