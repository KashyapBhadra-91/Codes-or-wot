def copy_with_uppercase(source_file, destination_file):
    try:
        with open(source_file, 'r') as src, open(destination_file, 'w') as dest:
            for line in src:
                dest.write(line.upper())
        print(f"Contents copied from '{source_file}' to '{destination_file}' with lowercase letters converted to uppercase.")
    except FileNotFoundError:
        print("Source file not found. Please check the path.")
    except Exception as e:
        print(f"An error occurred: {e}")

# Example usage
source_file = "input.txt"        # Replace with your source file path
destination_file = "output.txt"  # Replace with your destination file path

copy_with_uppercase(source_file, destination_file)
