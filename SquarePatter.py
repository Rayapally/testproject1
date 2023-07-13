def patterns(num):
    for i in range(num):
        for j in range(num):
            print("*",end = '')

        print()

n = int(input("Enter the number :"))
patterns(n)

