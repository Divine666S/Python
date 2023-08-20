# Prime numbers upto given number 
print("Prime numbres between 1 to 50")
for num in range(2, 51):
    is_prime = True
    flag = 2
    while flag * flag <= num:
        if num % flag == 0:
            is_prime = False
            break
        flag += 1
    if is_prime:
        print(num)
