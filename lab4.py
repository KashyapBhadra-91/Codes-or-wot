# 1) Create lists of odd and even numbers, replace, flatten, and print
odd_list = [random.randint(1, 50) * 2 + 1 for _ in range(5)]
even_list = [random.randint(1, 50) * 2 for _ in range(4)]
odd_list[2:3] = even_list  
flattened_list = odd_list  
print("1) Flattened List:", flattened_list)

# 2) Generate 20 random integers, find occurrences of a number
numbers = [random.randint(1, 100) for _ in range(20)]
num = int(input("Enter a number to find occurrences: "))
positions = [i for i, x in enumerate(numbers) if x == num]
print("2) Numbers:", numbers)
print("2) Positions of occurrences:", positions)

# 3) Generate 50 random numbers and remove duplicates
numbers = [random.randint(1, 30) for _ in range(50)]
unique_numbers = list(set(numbers))
print("3) Unique numbers:", unique_numbers)

# 4) Split 30 numbers into positive and negative lists
numbers = [random.randint(-50, 50) for _ in range(30)]
positive_numbers = [x for x in numbers if x >= 0]
negative_numbers = [x for x in numbers if x < 0]
print("4) Positive numbers:", positive_numbers)
print("4) Negative numbers:", negative_numbers)

# 5) Convert a list of strings to uppercase
strings = ["hello", "world", "python", "list", "example"]
uppercase_strings = [s.upper() for s in strings]
print("5) Uppercase strings:", uppercase_strings)

# 6) Convert Fahrenheit to Celsius
fahrenheit_list = [random.randint(32, 212) for _ in range(10)]
celsius_list = [(f - 32) * 5 / 9 for f in fahrenheit_list]
print("6) Celsius temperatures:", celsius_list)

# 7) Implement stack using list
stack = []
def push(item):
    stack.append(item)
def pop():
    if stack:
        return stack.pop()
    return "Stack is empty"
push(10)
push(20)
push(30)
print("7) Stack after push:", stack)
print("7) Popped item:", pop())
print("7) Stack after pop:", stack)

# 8) Implement queue using list
from collections import deque
queue = deque()
def enqueue(item):
    queue.append(item)
def dequeue():
    if queue:
        return queue.popleft()
    return "Queue is empty"
enqueue(10)
enqueue(20)
enqueue(30)
print("8) Queue after enqueue:", list(queue))
print("8) Dequeued item:", dequeue())
print("8) Queue after dequeue:", list(queue))

# 9) Create third list from numbers not in second list
list1 = [random.randint(1, 20) for _ in range(10)]
list2 = [random.randint(1, 20) for _ in range(5)]
list3 = [x for x in list1 if x not in list2]
print("9) List1:", list1)
print("9) List2:", list2)
print("9) List3 (filtered numbers):", list3)
