import pandas as pd

def excel_to_dict_with_total(filename):
    # Read the Excel file
    df = pd.read_excel(filename)

    # Initialize the dictionary
    student_dict = {}

    # Iterate over the rows and build the dictionary
    for index, row in df.iterrows():
        rollno = row['RollNo']
        name = row['Name']
        marks = [row['Subject1'], row['Subject2'], row['Subject3']]
        total = sum(marks)

        # Store in dictionary
        student_dict[rollno] = {
            'Name': name,
            'Marks': marks,
            'Total': total
        }

    return student_dict

# Example usage
file_path = 'students.xlsx'  # Make sure this file exists and has proper headers
data = excel_to_dict_with_total(file_path)

# Display the data
for rollno, info in data.items():
    print(f"Roll No: {rollno}")
    print(f"Name: {info['Name']}")
    print(f"Marks: {info['Marks']}")
    print(f"Total: {info['Total']}")
    print("-" * 30)
