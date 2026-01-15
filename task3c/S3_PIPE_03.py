# S3_PIPE_03.py
# Task: String normalization pipeline

import re

def pipe(*fns):
    """Apply functions left-to-right"""
    def piped(x):
        result = x
        for fn in fns:
            result = fn(result)
        return result
    return piped

def collapse_spaces(s):
    """Collapse multiple spaces into single space"""
    return re.sub(r'\s+', ' ', s)

def main():
    print("String Normalization Pipeline:")
    print("=" * 60)
    
    # Build pipeline: strip → lowercase → collapse spaces
    normalize = pipe(
        str.strip,
        str.lower,
        collapse_spaces
    )
    
    # Test cases
    test_strings = [
        " Ala  Ma   Kota ",
        "  HELLO    WORLD  ",
        "Multiple    Spaces   Between    Words",
        "  Normal  Text  ",
    ]
    
    for test_str in test_strings:
        result = normalize(test_str)
        print(f"Input:  '{test_str}'")
        print(f"Output: '{result}'")
        print("-" * 60)
    
    print("=" * 60)
    print("\nPipeline steps:")
    print("  1. strip() - remove leading/trailing whitespace")
    print("  2. lower() - convert to lowercase")
    print("  3. collapse_spaces() - replace multiple spaces with single space")

if __name__ == "__main__":
    main()