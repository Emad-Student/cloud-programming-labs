# S1_IF_01.py
# Task: Shipping cost calculator

def shipping_cost(weight_kg, is_member):
    """
    Calculate shipping cost based on weight and membership.
    
    Rules:
    - Invalid weight (not a number or <= 0) → return None
    - <= 1kg → 10
    - <= 5kg → 20
    - else → 30
    - Members get 20% discount
    """
    # Validate weight
    try:
        weight = float(weight_kg)
        if weight <= 0:
            return None
    except (ValueError, TypeError):
        return None
    
    # Determine base cost
    if weight <= 1:
        cost = 10
    elif weight <= 5:
        cost = 20
    else:
        cost = 30
    
    # Apply member discount
    if is_member:
        cost = cost * 0.8  # 20% discount
    
    return cost

def main():
    print("Shipping Cost Calculator Tests:")
    print("=" * 60)
    
    # Test cases (weight, is_member, description)
    tests = [
        (0.5, False, "0.5kg, non-member"),
        (1, False, "1kg boundary, non-member"),
        (1.1, False, "1.1kg, non-member"),
        (5, False, "5kg boundary, non-member"),
        (5.1, False, "5.1kg, non-member"),
        (10, False, "10kg, non-member"),
        (1, True, "1kg, member (with discount)"),
        (5, True, "5kg, member (with discount)"),
        (0, False, "Invalid: 0kg"),
        (-1, False, "Invalid: negative weight"),
        ("abc", False, "Invalid: not a number"),
        (None, False, "Invalid: None"),
    ]
    
    print(f"{'Weight':<10} {'Member':<8} {'Cost':<10} {'Description'}")
    print("-" * 60)
    
    for weight, is_member, desc in tests:
        cost = shipping_cost(weight, is_member)
        weight_str = str(weight)[:8]
        cost_str = f"${cost}" if cost is not None else "None"
        print(f"{weight_str:<10} {str(is_member):<8} {cost_str:<10} {desc}")
    
    print("=" * 60)

if __name__ == "__main__":
    main()
    