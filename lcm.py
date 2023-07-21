a = int(input("Enter the Number: "))
b = int(input("Enter the Number: "))

res = max(a,b)
while(res <= a * b):
    if(res % a == 0 and res % b == 0):
        break;
    res = res+1

print("The Lcm is : " , res)
