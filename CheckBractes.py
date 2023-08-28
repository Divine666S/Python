
# 1. Skill Program
# write a python code to check validity of string of bracess: --->> [()}

ol=["[","{","("]
cl=["]","}",")"]
def check(st):
    stk=[]
    for i in st:
        if i in ol:
            stk.append(i)
        elif i in cl:
            p=cl.index(i)
            if len(stk)>=0 and (ol[p]==stk[len(stk)-1]):
                stk.pop()
            else:
                return ("Unbalanced")
    if len(stk)==0:
        return("Balanced")
    else:
        return("Unbalanced")
str=input("Enter a string: ")
print(check(str))
# print(check("[()]"))
