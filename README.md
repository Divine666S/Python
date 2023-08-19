
# prime numbers B/W 1 to 50
print ("Prime numbers up to 50")
for i in range(2,51):
    c=0
    f=1
    while f<=i//2: # or while f<=2
        if i%f==0:
            c+=1
        f+=1
    if c==1: # or if c==2
        print(i)
