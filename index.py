def isSubstring(s1,s2):


    if s1 in s2:
        return s2.index(s1)
    return -1

if __name__ == "__main__":
    s1 = "for"
    s2 = "geeksforgeeks"
    res = isSubstring(s1, s2)
    if res == -1:
        print("Not present")
    else:
        print("Present at index " + str(res))