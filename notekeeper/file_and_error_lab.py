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


def count_lines(file_path):
    if not file_path.strip():
        raise ValueError("❌ Missing file path.")

    if not os.path.exists(file_path):  # ✅ Keep this
        raise FileNotFoundError(f"❌ File '{file_path}' not found.")  # ✅ Correction #2

    try:
        with open(file_path, 'r') as file:
            lines = [line for line in file if line.strip()]
            if not lines:
                raise ValueError("❌ The file is empty or has only blank lines.")
            return len(lines)
    except IOError as ioe:  # ✅
        print(f"❌ File read error: {ioe}")
        return None
