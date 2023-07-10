'''n = str(input("Enter the name :"))
for i in n:
    if i == 'h':
        pass
        print("this is substring ")
    print("current leters",i)
print("bye")'''

def pass_statement(name):
    for i in name:
        if i == 'a':
            pass
        print(i,end=' ')


name = str(input("Enter the name :"))
pass_statement(name)

