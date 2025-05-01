def count_vowels(s, index=0):
    vowels = "aeiouAEIOU"
    if index == len(s):
        return 0
    return (s[index] in vowels) + count_vowels(s, index + 1)
text = input("Enter a string: ")
print("Number of vowels:", count_vowels(text))
