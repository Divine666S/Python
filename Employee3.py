# Employe Class -->
class Employee:
    def __init__ (self, name, id, salary):
        self.name=name
        self.id=id
        self.salary=salary

    def display(self):
        print("Name: ", self.name)
        print("I'd: ", self.id)
        print("Salary: ", self.salary)
    
#Taking Input from user: --> 
name=input("Enter  Name: ")
id=int(input("Enter  I'd: "))
salary=float(input("Enter  Salary: "))

#Creating Object -->
employee=Employee(name, id, salary)

# Displaying Details -->
employee.display()