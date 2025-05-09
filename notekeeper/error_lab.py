def value_error_example():
    try:
        number = int(input("Enter an integer: "))
        print(f"You entered: {number}")
    except ValueError:
        print("❌ That's not a valid integer.")

def zero_division_example():
    try:
        x = float(input("Enter numerator: "))
        y = float(input("Enter denominator: "))
        print("Result:", x / y)
    except ZeroDivisionError:
        print("❌ You cannot divide by zero.")
    except ValueError:
        print("❌ Please enter numbers only.")

def raise_example():
    age = input("Enter your age: ").strip()
    if not age.isdigit():
        raise ValueError("❌ Age must be a number.")
    print(f"✅ You entered age: {age}")

def file_not_found_example():
    try:
        name = input("Enter a file name to open: ")
        with open(name, "r") as file:
            print(file.read())
    except FileNotFoundError:
        print("❌ File not found.")

def type_error_example():
    try:
        value = input("Enter a number: ")
        result = value + 5  # wrong: str + int
    except TypeError:
        print("❌ You cannot add a number to text.")

def combined_finally_example():
    try:
        n = int(input("Enter a positive number: "))
        if n < 0:
            raise ValueError("Number must be positive")
        print(f"Square is {n ** 2}")
    except ValueError as ve:
        print(f"❌ {ve}")
    finally:
        print("✅ Finished the block.")


