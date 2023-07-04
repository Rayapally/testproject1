x = int(input("enter number:"))
sum = 0
temp = x


while(x > 0):

    res = x % 10 #it will give last digit
    sum = sum *10 + res
    x //= 10
# it will give --- reverse number
print(str(sum))

# it will give the  pallindrome or not
if(temp == sum):
    print("is pallindrome")
else:
    print("it was not pallindrome")

