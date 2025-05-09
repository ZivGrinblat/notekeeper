import os


def read_file(file_path):
    """
    Safely reads and prints the contents of a file.
    Raises:
        ValueError: If the file path is empty or file is empty.
        FileNotFoundError: If the file doesn't exist.
    """
    if not file_path.strip():  # ✅ Correction #1
        raise ValueError("❌ Missing file path.")

    if not os.path.exists(file_path):  # ✅ Keep this
        raise FileNotFoundError(f"❌ File '{file_path}' not found.")  # ✅ Correction #2

    try:
        with open(file_path, 'r') as file:
            lines = file.readlines()
            if not lines:
                raise ValueError("❌ The file is empty.")  # ✅ Correction #3

            print("📄 File content:")
            for line in lines:
                print(line, end='')  # ✅ Good use
    except IOError as ioe:  # ✅ Correction #4
        print(f"❌ File read error: {ioe}")


import os


def count_lines(file_path):
    """
    Counts non-empty lines in a file.

    Raises:
        ValueError: If path is missing or file is empty.
        FileNotFoundError: If file does not exist.
    """
    if not file_path.strip():
        raise ValueError("❌ Missing file path.")

    if not os.path.exists(file_path):
        raise FileNotFoundError(f"❌ File '{file_path}' not found.")

    try:
        with open(file_path, 'r') as file:
            lines = [line for line in file if line.strip()]  # ✅ Now referencing 'file', not 'lines'

            if not lines:
                raise ValueError("❌ The file is empty or has only blank lines.")
            return len(lines)
    except IOError as ioe:
        print(f"❌ File read error: {ioe}")
        return None


import os

def append_user_note(file_path):
    """
    Appends a user note to the specified file.
    Raises:
        ValueError: If path or content is missing.
    """
    if not file_path.strip():
        raise ValueError("❌ Missing file path.")

    try:
        user_input = input("📝 Please enter your note: ").strip()
        if not user_input:
            raise ValueError("❌ Note cannot be empty.")

        with open(file_path, 'a') as file:
            file.write(user_input + '\n')

    except IOError as ioe:
        print(f"❌ File write error: {ioe}")
    else:
        print(f"✅ Note added to {file_path}")

