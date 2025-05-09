import os.path
from pyexpat.errors import messages

from matplotlib.lines import lineStyles


def ensure_file_exists(file_name, default_text="Placeholder note.\n"):
    if not os.path.exists(file_name):
        with open(file_name, 'w') as file:
            file.write(default_text)


def add_note(file_name):
    try:
        note = input("Write your note: ").strip()
        if not note:
            raise ValueError("Note cannot be empty")
        ensure_file_exists(file_name)
        with open(file_name, 'a') as file:
            file.write(note + "\n")
    except ValueError as ve:
        print(f"ERROR: {ve}")
    except IOError as ioe:
        print(f"❌ File write error: {ioe}")
    else:
        print("✅ Note added successfully.")


def append_to_last_note(file_name):
    try:
        text = input("➕ Text to append to last note: ").strip()
        if not text:
            raise ValueError("Text cannot be empty")

        ensure_file_exists(file_name)
        with open(file_name, 'r') as file:
            lines = file.readlines()

        if not lines:
            raise ValueError("There are no notes to append to")

        lines[-1] = lines[-1].rstrip("\n") + " " + text + "\n"

        with open(file_name, 'w') as file:
            file.writelines(lines)

    except ValueError as ve:
        print(f"❌ Error: {ve}")
    except IOError as ioe:
        print(f"❌ File error: {ioe}")
    else:
        print(f"✅ Text appended to the last line in {file_name}")


if __name__ == "__main__":
    NOTES_FILE = "notes.txt"
    print("1. Add note\n2. Append to last note")
    choice = input("Choose an option: ").strip()

    try:
        if choice not in ['1', '2']:
            raise ValueError("Choose one of the two, please")

        if choice == "1":
            message = add_note(NOTES_FILE)
        elif choice == "2":
            message = append_to_last_note(NOTES_FILE)

        print(message)

    except ValueError as ve:
        print(f"❌ {ve}")
        exit(1)
