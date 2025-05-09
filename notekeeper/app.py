def add_note():
    try:
        note = input("Write your note: ").strip()
        if not note:
            raise ValueError("Note cannot be empty")
        with open("notes.txt", 'a') as file:
            file.write(note + "\n")
    except ValueError as ve:
        print(f"ERROR: {ve}")
    except IOError as ioe:
        print(f"❌ File write error: {ioe}")
    else:
        print("✅ Note added successfully.")

if __name__ == "__main__":
    add_note()
