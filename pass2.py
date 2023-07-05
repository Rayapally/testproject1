'''x  = int(input("Enter the number:"))
y  = int(input("Enter the number:"))

days = (x-y)% 7

print(days)'''

def main(days,num):
    res = (days - num) % 7
    print(res)
days = int(input("Enter the days :"))
num = int(input("Enter the number :"))
main(days,num)