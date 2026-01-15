# S3_PIPE_04.py
# Task: Iterable pipeline (generator-based)

def parse_and_convert(values):
    """
    Generator that strips strings and converts to float.
    Skips values that fail conversion.
    """
    for value in values:
        try:
            trimmed = value.strip()
            number = float(trimmed)
            yield number
        except (ValueError, AttributeError):
            # Skip invalid values
            pass

def double_values(values):
    """Generator that doubles each value"""
    for value in values:
        yield value * 2

def main():
    print("Iterable Pipeline (Generator-based):")
    print("=" * 60)
    
    # Input data with numbers and junk
    data = [
        " 10 ",
        "20",
        "abc",
        " 30.5 ",
        "xyz",
        "  15  ",
        "invalid",
        "25"
    ]
    
    print(f"Input data: {data}")
    print("-" * 60)
    
    # Build pipeline using generators
    print("\nProcessing pipeline:")
    print("  1. Strip whitespace and convert to float (skip failures)")
    print("  2. Double each value")
    print("  3. Sum all values")
    print("-" * 60)
    
    # Apply pipeline
    parsed = parse_and_convert(data)
    doubled = double_values(parsed)
    total = sum(doubled)
    
    print(f"\nFinal sum: {total}")
    
    # Show step-by-step for clarity
    print("\nStep-by-step breakdown:")
    parsed_list = list(parse_and_convert(data))
    print(f"  After parsing: {parsed_list}")
    doubled_list = [x * 2 for x in parsed_list]
    print(f"  After doubling: {doubled_list}")
    print(f"  After sum: {sum(doubled_list)}")
    
    print("=" * 60)
    print("\nNote: Generators process items one at a time,")
    print("which is memory-efficient for large datasets.")

if __name__ == "__main__":
    main()