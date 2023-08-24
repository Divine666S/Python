
#student class where only one class is ther and create 2 objects and print 2 students details.

class Student1: 
    name = ""
    rollno = 0
    branch = ""

s1 = Student1()
s1.name = input("Enter the name for Student 1: ")
s1.rollno = int(input("Enter the roll no of Student 1: "))
s1.branch = input("Enter the branch name of Student 1: ")

print("\nStudent1 detail:")
print("Name:", s1.name)
print("Roll no:", s1.rollno)
print("Branch:", s1.branch)

s2 = Student1()
s2.name = input("\nEnter the name for Student 2: ")
s2.rollno = int(input("Enter the roll no of Student 2: "))
s2.branch = input("Enter the branch name of Student 2: ")

print("\nStudent2 detail:")
print("Name:", s2.name)
print("Roll no:", s2.rollno)
print("Branch:", s2.branch)
