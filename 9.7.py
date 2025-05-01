def average_list(lst, index=0, total=0):
    if index == len(lst):
        return total / len(lst) if lst else 0
    return average_list(lst, index + 1, total + lst[index])
numbers = list(map(int, input("Enter a list of numbers separated by spaces: ").split()))
print("Average of list:", average_list(numbers))
