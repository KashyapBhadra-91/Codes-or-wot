import csv
# Data to write into CSV
data = [
["Name", "Subject", "Score"],
["Alice", "Math", 90],
["Bob", "Science", 85],
["Charlie", "History", 78],
["Diana", "English", 92]
]
# Creating CSV file
filename = "students_scores.csv"
with open(filename, mode="w", newline="") as file:
writer = csv.writer(file)
writer.writerows(data)
print(f"CSV file '{filename}' created successfully.")
