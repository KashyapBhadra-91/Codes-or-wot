def sanitize_list(lst, index=0):
    if index == len(lst):
        return lst
    if lst[index] < 0:
        lst[index] = 0
    return sanitize_list(lst, index + 1)
numbers = list(map(int, input("Enter a list of numbers separated by spaces: ").split()))
sanitize_list(numbers)
print("Sanitized list:", numbers)
