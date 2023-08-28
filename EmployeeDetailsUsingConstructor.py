class Employee:
    def __init__(self, name, emp_id, salary):
        self.name = name
        self.emp_id = emp_id
        self.salary = salary

    def display(self):
        print("Name:", self.name)
        print("ID:", self.emp_id)
        print("Salary:", self.salary)
        print()

# Creating employee objects
employee1 = Employee("Sachin", 56, 50000)
employee2 = Employee("Kartik", 214, 60000)
employee3 = Employee("Gaurav", 177, 55000)

# Displaying employee details
print("Employee 1 details:")
employee1.display()

print("Employee 2 details:")
employee2.display()

print("Employee 3 details:")
employee3.display()
