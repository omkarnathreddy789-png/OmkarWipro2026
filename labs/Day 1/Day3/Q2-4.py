def write_numbers_to_file(filename):
    try:
        with open(filename, "w", encoding="utf-8") as f:
            for i in range(1, 101):
                f.write(f"{i}\n")
        print("Numbers written successfully.")

    except FileNotFoundError:
        print("Error: File not found.")

    except PermissionError:
        print("Error: Permission denied.")


def read_file_safely(filename):
    try:
        with open(filename, "r", encoding="utf-8") as f:
            print("\nFile contents:")
            print(f.read())

    except FileNotFoundError:
        print("Error: File not found while reading.")

    except PermissionError:
        print("Error: Permission denied while reading.")


# Main execution
filename = "number.txt"

write_numbers_to_file(filename)
read_file_safely(filename)
