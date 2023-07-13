def func(num): #func --- > sum of natural numbers
    sum = 0 # take a zero variable
    while (num > 0):
        sum = sum + num
        num = num - 1
    return sum
num =int(input("Enter the number :"))

res = func(num)

print(res)