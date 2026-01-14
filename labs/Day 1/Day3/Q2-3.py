def write_numbers_to_file(filename):
    """
    Writes numbers from 1 to 100 into a file
    and handles possible exceptions.
    """
    try:
        with open(filename, "w", encoding="utf-8") as f:
            for i in range(1, 101):
                f.write(f"{i}\n")

        print("Numbers written successfully.")

    except FileNotFoundError:
        print("Error: File not found.")

    except PermissionError:
        print("Error: Permission denied.")

    except Exception as e:
        print("Unexpected error:", e)



write_numbers_to_file("nums.txt")
