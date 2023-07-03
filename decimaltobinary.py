# DectoBin means Decimal to Binary

def DectoBin(num):
    if num > 1:
        DectoBin(num // 2)
    print(num % 2 , end = ' ')
dec = 10
DectoBin(dec)
print()