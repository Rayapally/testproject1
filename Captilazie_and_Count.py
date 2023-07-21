def Cap_and_Count(S):
    print(S.title().strip())
    print(len(S.split(" ")))

S = str(input("Enter the String"))
print(Cap_and_Count(S))
