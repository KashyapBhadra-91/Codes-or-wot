# Task 1
words = ["apple", "banana", "cherry", "date"]
uppercase_set = {word.upper() for word in words}
print(uppercase_set)

# Task 2
import random
random_numbers = {random.randint(15, 45) for _ in range(10)}
count_less_than_30 = sum(1 for num in random_numbers if num < 30)
random_numbers = {num for num in random_numbers if num <= 35}
print(count_less_than_30, random_numbers)

# Task 3
names_set = set()
names_set.update({"Alice", "Bob", "Charlie", "David", "Eve"})
names_set.discard("Alice")
names_set.discard("Bob")
names_set.add("Anna")
print(names_set)

# Task 4
names = {"Alice", "Andrew", "Ben", "Barbara", "Alex", "Brian"}
a_names = {name for name in names if name.startswith("A")}
b_names = {name for name in names if name.startswith("B")}
print(a_names, b_names)
