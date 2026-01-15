# S1_VAR_01.py
# Task: Catalog of values and type()

def main():
    # Create variables of different types
    my_int = 42
    my_float = 3.14
    my_str = "hello"
    my_bool = True
    my_none = None
    my_list = [1, 2, 3]
    my_tuple = (4, 5, 6)
    my_dict = {"key": "value"}
    my_set = {7, 8, 9}
    my_function = lambda x: x * 2
    
    # Create a list of all variables with their names
    variables = [
        ("my_int", my_int),
        ("my_float", my_float),
        ("my_str", my_str),
        ("my_bool", my_bool),
        ("my_none", my_none),
        ("my_list", my_list),
        ("my_tuple", my_tuple),
        ("my_dict", my_dict),
        ("my_set", my_set),
        ("my_function", my_function),
    ]
    
    # Print table header
    print("=" * 70)
    print(f"{'Name':<15} {'Value':<20} {'type(x)':<25} {'type(x).__name__'}")
    print("=" * 70)
    
    # Print each variable's information
    for name, value in variables:
        value_str = str(value)[:18]  # Truncate long values
        type_str = str(type(value))
        type_name = type(value).__name__
        print(f"{name:<15} {value_str:<20} {type_str:<25} {type_name}")
    
    print("=" * 70)

if __name__ == "__main__":
    main()