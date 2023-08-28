
# >> 3 Object for one Employee class and displaying the Details of an Employee --->

print("\nEmployee Details: \n")

class Employee:
    name=""
    id=0
    salary=0

# >> Createing an Object and Taking Details of Employees from user----->>

e1=Employee()
print("Enter the frist Employee Details:")
e1.name=input("name: ")
e1.id=input("i'd: ")
e1.salary=input("salary: ")

e2=Employee()
print("\nEnter the Second Employee Details:")
e2.name=input("name: ")
e2.id=input("i'd: ")
e2.salary=input("salary: ")

e3=Employee()
print("\nEnter the Third Employee Details:")
e3.name=input("name: ")
e3.id=input("i'd: ")
e3.salary=input("salary: ")

# >> Printing the details of Employees---->
# Frist Employee:

print("\nFirst Employee Details: \n")
print("Name: ",e1.name)
print("I'd: ",e1.id)
print("Salary: ",e1.salary)

# Second Employee:

print("\nSecond Employee Details: \n")
print("Name: ",e2.name)
print("I'd: ",e2.id)
print("Salary: ",e2.salary)
# Third Employee:

print("\nThird Employee Details: \n")
print("Name: ",e3.name)
print("I'd: ",e3.id)
print("Salary: ",e3.salary)
