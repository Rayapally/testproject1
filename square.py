def square(num):

    for i in range(num):
        for j in range(num):
            print("*",end='')
        print()


num = int(input("Enter the number:"))
res=square(num)
print(res)
