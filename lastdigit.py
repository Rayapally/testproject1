x = int(input("enter number:"))
sum = 0


while(x != 0):

    res = x % 10
    sum = sum *10 + res
    x //= 10




print(str(sum))
