print("Grade Sheet")
print("Enter the marks: ")
py=int(input())
math=int(input())
java=int(input())
ds=int(input())
os=int(input())

avg= (py+math+java+ds+os)/5

if py<=40 or math<=40 or java<=40 or ds<=40 or os<=40:
    print("Fail")
elif avg>=75:
    print("Distiction")
elif avg<=74 and avg>=65:
    print("Frist Class")
elif avg<=64 and avg>=55:
    print("Second Class")
elif avg<=54 and avg>=39:
    print("Third Class")
else:
    print("Fail")