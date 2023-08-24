def factorial(n):
    return n * factorial(n - 1) if n > 0 else 1

print("Factorial using Recursion function:")
num = int(input("Enter the number: "))
result = factorial(num)
print("Factorial =", result)
