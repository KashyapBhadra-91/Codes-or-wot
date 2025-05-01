def string_length(s, index=0):
    if index == len(s):
        return index
    return string_length(s, index + 1)

# Receive input string from user
text = input("Enter a string: ")

# Compute and print length
print("Length of string:", string_length(text))
