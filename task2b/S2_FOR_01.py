# S2_FOR_01.py
# Task: FizzBuzz+

def fizzbuzz(n):
    """
    Print FizzBuzz for numbers 1 to n.
    - Multiples of 3: "Fizz"
    - Multiples of 5: "Buzz"
    - Multiples of both: "FizzBuzz"
    - Otherwise: the number
    """
    for i in range(1, n + 1):
        if i % 3 == 0 and i % 5 == 0:
            print("FizzBuzz")
        elif i % 3 == 0:
            print("Fizz")
        elif i % 5 == 0:
            print("Buzz")
        else:
            print(i)

def main():
    print("FizzBuzz (1 to 30):")
    print("=" * 40)
    fizzbuzz(30)
    print("=" * 40)

if __name__ == "__main__":
    main()
    