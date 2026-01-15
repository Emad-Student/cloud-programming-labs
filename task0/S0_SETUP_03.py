# S0_SETUP_03.py
# Task: Minimal test helper function

def eq(actual, expected, message=""):
    """
    Simple equality test helper.
    Raises AssertionError if actual != expected.
    """
    if actual != expected:
        error_msg = f"Test failed: expected {expected}, got {actual}"
        if message:
            error_msg = f"{message} - {error_msg}"
        raise AssertionError(error_msg)
    print(f"✓ Test passed: {actual} == {expected}")

# Test the helper itself
def main():
    print("Testing eq() helper function:")
    print("-" * 40)
    
    # These should pass
    eq(5, 5, "Integer equality")
    eq("hello", "hello", "String equality")
    eq([1, 2], [1, 2], "List equality")
    
    # This will fail (uncomment to see error)
    # eq(5, 6, "This should fail")
    
    print("-" * 40)
    print("All tests passed! Helper function works.")

if __name__ == "__main__":
    main()