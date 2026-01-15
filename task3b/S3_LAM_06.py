# S3_LAM_06.py
# Task: Map values in a dict

def map_values(d, fn):
    """
    Apply a function to all values in a dict.
    Returns a new dict with transformed values.
    Uses dict comprehension.
    """
    return {k: fn(v) for k, v in d.items()}

def main():
    print("Map Values in Dict Tests:")
    print("=" * 60)
    
    # Test 1: Double all numbers
    prices = {"apple": 1.5, "banana": 0.75, "orange": 2.0}
    doubled = map_values(prices, lambda x: x * 2)
    
    print("Test 1: Double all prices")
    print(f"  Original: {prices}")
    print(f"  Doubled:  {doubled}")
    print("-" * 60)
    
    # Test 2: Uppercase all strings
    names = {"first": "alice", "last": "smith", "middle": "jane"}
    uppercase = map_values(names, lambda x: x.upper())
    
    print("\nTest 2: Uppercase all names")
    print(f"  Original:  {names}")
    print(f"  Uppercase: {uppercase}")
    print("-" * 60)
    
    # Test 3: Square all numbers
    scores = {"math": 8, "physics": 9, "chemistry": 7}
    squared = map_values(scores, lambda x: x ** 2)
    
    print("\nTest 3: Square all scores")
    print(f"  Original: {scores}")
    print(f"  Squared:  {squared}")
    print("=" * 60)

if __name__ == "__main__":
    main()