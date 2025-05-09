import os


def ensure_file_exists(file_name, default_text="Placeholder note.\n"):
    if not os.path.exists(file_name):
        with open(file_name, 'w') as file:
            file.write(default_text)


def get_filename_from_user():
    file_name = input("📄 Enter the file name you'd like to use (e.g., notes.txt): ").strip()
    if not file_name:
        raise ValueError("Filename cannot be empty.")
    return file_name


def add_note(file_name):
    try:
        note = input("📝 Write your note: ").strip()
        if not note:
            raise ValueError("Note cannot be empty.")
        ensure_file_exists(file_name)
        with open(file_name, 'a') as file:
            file.write(note + "\n")
    except ValueError as ve:
        return f"❌ {ve}"
    except IOError as ioe:
        return f"❌ File write error: {ioe}"
    else:
        return "✅ Note added successfully."


def append_note(file_name):
    try:
        text = input("➕ Enter a note to add as a new line: ").strip()
        if not text:
            raise ValueError("Text cannot be empty.")
        ensure_file_exists(file_name)
        with open(file_name, 'a') as file:
            file.write(text + "\n")
    except ValueError as ve:
        return f"❌ {ve}"
    except IOError as ioe:
        return f"❌ File write error: {ioe}"
    else:
        return f"✅ New line added to {file_name}"


if __name__ == "__main__":
    try:
        file_name = get_filename_from_user()

        print("\nChoose an action:")
        print("1. Add note")
        print("2. Append to file")
        choice = input("Your choice (1/2): ").strip()

        if choice not in ['1', '2']:
            raise ValueError("Invalid option. Please choose 1 or 2.")

        if choice == '1':
            message = add_note(file_name)
        elif choice == '2':
            message = append_note(file_name)

        print(message)

    except ValueError as ve:
        print(f"❌ {ve}")
        exit(1)
