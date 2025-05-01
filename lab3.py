# 1) Count how many vowels are in a string  
def count_vowels(s):  
    vowels = "aeiouAEIOU"  
    count = 0  
    for ch in s:  
        if ch in vowels:  
            count += 1  
    return count  

str1 = input("Enter a string: ")  
print("1) Number of vowels:", count_vowels(str1))  

# 2) Convert all characters to lower case, upper case, and toggle case  
def to_lower(s):  
    result = ""  
    for ch in s:  
        if 'A' <= ch <= 'Z':  
            result += chr(ord(ch) + 32)  
        else:  
            result += ch  
    return result  

def to_upper(s):  
    result = ""  
    for ch in s:  
        if 'a' <= ch <= 'z':  
            result += chr(ord(ch) - 32)  
        else:  
            result += ch  
    return result  

def toggle_case(s):  
    result = ""  
    for ch in s:  
        if 'A' <= ch <= 'Z':  
            result += chr(ord(ch) + 32)  
        elif 'a' <= ch <= 'z':  
            result += chr(ord(ch) - 32)  
        else:  
            result += ch  
    return result  

print("2) Lowercase:", to_lower(str1))  
print("2) Uppercase:", to_upper(str1))  
print("2) Toggle case:", toggle_case(str1))  

# 3) Check whether one string is in another  
def is_substring(str1, str2):  
    if str2 in str1:  
        return True  
    return False  

main_str = input("Enter the main string: ")  
sub_str = input("Enter the substring to check: ")  

if is_substring(main_str, sub_str):  
    print("3) Substring is present.")  
else:  
    print("3) Substring is not present.")  

# 4) Remove one string from another string if present  
def remove_substring(main_str, remove_str):  
    result = main_str.replace(remove_str, "")  
    return result  

remove_str = input("Enter the string to remove: ")  
print("4) Resulting string:", remove_substring(main_str, remove_str))
