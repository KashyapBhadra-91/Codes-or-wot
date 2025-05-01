def remove_articles(input_file, output_file):
    articles = {'a', 'an', 'the'}

    try:
        with open(input_file, 'r') as infile:
            content = infile.read()

        words = content.split()
        filtered_words = [word for word in words if word.lower() not in articles]

        new_content = ' '.join(filtered_words)
        with open(output_file, 'w') as outfile:
            outfile.write(new_content)

        print(f"Articles removed and content saved to '{output_file}'.")

    except FileNotFoundError:
        print("Input file not found. Please check the path.")
    except Exception as e:
        print(f"An error occurred: {e}")


input_file = "input.txt"       
output_file = "output.txt"     

remove_articles(input_file, output_file)
