# S1_IF_02.py
# Task: Score to grade converter

def grade(score):
    """
    Convert a numeric score (0-100) to a letter grade.
    
    Grading scale:
    - A: 90-100
    - B: 80-89
    - C: 70-79
    - D: 60-69
    - F: 0-59
    - Outside range: None
    """
    # Validate score
    if not isinstance(score, (int, float)):
        return None
    
    if score < 0 or score > 100:
        return None
    
    # Determine grade
    if score >= 90:
        return "A"
    elif score >= 80:
        return "B"
    elif score >= 70:
        return "C"
    elif score >= 60:
        return "D"
    else:
        return "F"

def main():
    print("Grade Calculator - Boundary Tests:")
    print("=" * 40)
    
    # Test cases including all boundaries
    test_scores = [
        59,   # F (just below D)
        60,   # D (lower boundary)
        69,   # D (upper boundary)
        70,   # C (lower boundary)
        79,   # C (upper boundary)
        80,   # B (lower boundary)
        89,   # B (upper boundary)
        90,   # A (lower boundary)
        100,  # A (max valid)
        101,  # Invalid (above max)
        -1,   # Invalid (below min)
        0,    # F (min valid)
    ]
    
    print(f"{'Score':<10} {'Grade':<10} {'Notes'}")
    print("-" * 40)
    
    for score in test_scores:
        result = grade(score)
        if result is None:
            notes = "Invalid score"
        elif score in [60, 70, 80, 90]:
            notes = "Lower boundary"
        elif score in [59, 69, 79, 89]:
            notes = "Upper boundary"
        elif score == 100:
            notes = "Maximum score"
        else:
            notes = ""
        
        print(f"{score:<10} {str(result):<10} {notes}")
    
    print("=" * 40)

if __name__ == "__main__":
    main()
    