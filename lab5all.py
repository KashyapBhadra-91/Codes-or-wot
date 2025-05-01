import random  

odd_numbers = [random.randint(1, 50) * 2 + 1 for _ in range(5)]  
print("Original list of 5 odd integers:", odd_numbers)  

even_numbers = [random.randint(1, 50) * 2 for _ in range(4)]  
print("Generated list of 4 even integers:", even_numbers)  

odd_numbers[2] = even_numbers  
print("List after replacing third element with even numbers:", odd_numbers)  

flattened_list = []  
for item in odd_numbers:  
    if isinstance(item, list):  
        flattened_list.extend(item)  
    else:  
        flattened_list.append(item)  

print("Flattened list:", flattened_list)  

flattened_list.sort()  
print("Sorted final list:", flattened_list)
print("--------------------------------------------------------------------------")  
numbers = [random.randint(1, 100) for _ in range(20)]  
print("Generated list:", numbers)  
search_num = int(input("Enter a number to search: "))  
positions = [i for i, num in enumerate(numbers) if num == search_num]  
print("Positions of occurrences:", positions)
print("--------------------------------------------------------------------------")

random_numbers = [random.randint(1, 30) for _ in range(50)]  
unique_numbers = list(set(random_numbers))  
print("List after removing duplicates:", unique_numbers)  
print("--------------------------------------------------------------------------")
 
random_numbers = [random.randint(-50, 50) for _ in range(30)]  
positive_numbers = [num for num in random_numbers if num > 0]  
negative_numbers = [num for num in random_numbers if num < 0]  
print("Positive numbers:", positive_numbers)  
print("Negative numbers:", negative_numbers)  
print("--------------------------------------------------------------------------")
 
string_list = ["hello", "world", "python", "programming", "task"]  
uppercase_list = [s.upper() for s in string_list]  
print("Uppercase strings:", uppercase_list)  
print("--------------------------------------------------------------------------")
  
fahrenheit_temps = [random.uniform(32, 100) for _ in range(10)]  
celsius_temps = [(f - 32) * 5/9 for f in fahrenheit_temps]  
print("Temperatures in Celsius:", celsius_temps)  
print("--------------------------------------------------------------------------")
 
stack = []  
while True:  
    print("\nStack Operations: 1. Push 2. Pop 3. Display 4. Exit")  
    choice = int(input("Enter choice: "))  
    if choice == 1:  
        stack.append(int(input("Enter number to push: ")))  
    elif choice == 2:  
        if stack:  
            print("Popped:", stack.pop())  
        else:  
            print("Stack is empty")  
    elif choice == 3:  
        print("Stack contents:", stack)  
    elif choice == 4:  
        break  
print("--------------------------------------------------------------------------")

from collections import deque  
queue = deque()  
while True:  
    print("\nQueue Operations: 1. Enqueue 2. Dequeue 3. Display 4. Exit")  
    choice = int(input("Enter choice: "))  
    if choice == 1:  
        queue.append(int(input("Enter number to enqueue: ")))  
    elif choice == 2:  
        if queue:  
            print("Dequeued:", queue.popleft())  
        else:  
            print("Queue is empty")  
    elif choice == 3:  
        print("Queue contents:", list(queue))  
    elif choice == 4:  
        break  
print("--------------------------------------------------------------------------")
 
list1 = [random.randint(1, 20) for _ in range(10)]  
list2 = [random.randint(1, 20) for _ in range(10)]  
list3 = [num for num in list1 if num not in list2]  
print("First list:", list1)  
print("Second list:", list2)  
print("Numbers in first list not in second:", list3)
print("--------------------------------------------------------------------------")
