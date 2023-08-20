#Python code to find prime numbers between a starting and ending number provided by the user

start = int(input("Enter the Starting Number: "))
end = int(input("Enter the Ending Number: "))

print("Prime numbers between", start, "and", end, "are:")

for num in range(start, end + 1):
    c = 0
    f = 1
    while f <= num // 2:
        if num % f == 0:
            c += 1
        f += 1
    if c == 1:
        print(num)
