def write_numbers_to_file(filename):
    """
    Write numbers from 1 to 100 to a file,
    one number per line.
    """
    with open(filename, "w", encoding="utf-8") as f:
        for i in range(1, 101):
            f.write(f"{i}\n")

# Example usage
write_numbers_to_file("num.txt")
print("Numbers 1–100 have been written to numbers.txt")
