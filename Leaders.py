def Leader(A):
    
    N = len(A) # A ---- > Array , N ---> Length of an Array
    ans = []
    maxx = A[N-1]

    for i in range(N-1,-1,-1):
        if A[i] >= maxx:
            maxx = A[i]

            ans.append(maxx)

    ans.reverse()
    return ans

A = [16,17,4,3,5,2]

res = Leader(A)

print(res)