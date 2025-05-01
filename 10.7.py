import pickle

# Define the Employee class
class Employee:
    def _init_(self, empcode, empname, doj, salary):
        self.empcode = empcode
        self.empname = empname
        self.doj = doj
        self.salary = salary

    def display(self):
        print(f"Emp Code: {self.empcode}")
        print(f"Name: {self.empname}")
        print(f"Date of Joining: {self.doj}")
        print(f"Salary: {self.salary}")

# Function to serialize employee data
def serialize_employee(employee, filename):
    with open(filename, 'wb') as file:
        pickle.dump(employee, file)
    print(f"Employee data serialized to '{filename}'.")

# Function to deserialize employee data
def deserialize_employee(filename):
    with open(filename, 'rb') as file:
        employee = pickle.load(file)
    print("Employee data deserialized successfully.")
    return employee

# Example usage
emp = Employee("E001", "Alice", "2021-07-15", 55000)

# Serialize the object
serialize_employee(emp, "employee.dat")

# Deserialize and display
emp_loaded = deserialize_employee("employee.dat")
emp_loaded.display()
