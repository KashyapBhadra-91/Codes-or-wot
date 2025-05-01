def merge_alternate_lines(file1, file2, output_file):
    try:
        with open(file1, 'r') as f1, open(file2, 'r') as f2:
            lines1 = f1.readlines()
            lines2 = f2.readlines()

        merged_lines = []

        # Get the maximum length of the two
        max_len = max(len(lines1), len(lines2))

        for i in range(max_len):
            if i < len(lines1):
                merged_lines.append(lines1[i])
            if i < len(lines2):
                merged_lines.append(lines2[i])

        # Write to output file
        with open(output_file, 'w') as out:
            out.writelines(merged_lines)

        print(f"Lines merged into '{output_file}' successfully.")

    except FileNotFoundError:
        print("One of the files was not found. Please check the file paths.")
    except Exception as e:
        print(f"An error occurred: {e}")

# Example usage
file1 = "file1.txt"           # Replace with your actual file path
file2 = "file2.txt"           # Replace with your actual file path
output_file = "merged.txt"    # The target output file

merge_alternate_lines(file1, file2, output_file)
