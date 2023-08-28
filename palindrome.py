
#Palindrome number using python

num = int(input("Enter a value:"))
temp = num
rev = 0

while num > 0:
    rem = num % 10
    rev = rev * 10 + rem
    num = num // 10

if temp == rev:
    print("This is a palindrome number!")
else:
    print("This is not a palindrome number!")
