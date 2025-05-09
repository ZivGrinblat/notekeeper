from error_lab import (
    value_error_example,
    zero_division_example,
    raise_example,
    file_not_found_example,
    type_error_example,
    combined_finally_example
)

if __name__ == "__main__":
    print("🔬 Choose a test:")
    print("1. ValueError")
    print("2. ZeroDivisionError")
    print("3. Raise manually")
    print("4. FileNotFoundError")
    print("5. TypeError")
    print("6. Combined + finally")

    choice = input("Run test (1–6): ").strip()

    if choice == "1":
        value_error_example()
    elif choice == "2":
        zero_division_example()
    elif choice == "3":
        raise_example()
    elif choice == "4":
        file_not_found_example()
    elif choice == "5":
        type_error_example()
    elif choice == "6":
        combined_finally_example()
    else:
        print("❌ Invalid choice.")
