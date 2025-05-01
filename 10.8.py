def remove_articles(input_file, output_file):
    articles = {'a', 'an', 'the'}

    try:
        with open(input_file, 'r') as infile:
            content = infile.read()

        # Split content into words and remove articles
        words = content.split()
        filtered_words = [word for word in words if word.lower() not in articles]

        # Join the filtered words back into text
        new_content = ' '.join(filtered_words)

        # Write to the output file
        with open(output_file, 'w') as outfile:
            outfile.write(new_content)

        print(f"Articles removed and content saved to '{output_file}'.")

    except FileNotFoundError:
        print("Input file not found. Please check the path.")
    except Exception as e:
        print(f"An error occurred: {e}")

# Example usage
input_file = "input.txt"       # Replace with your actual input file path
output_file = "output.txt"     # Replace with desired output file name

remove_articles(input_file, output_file)
