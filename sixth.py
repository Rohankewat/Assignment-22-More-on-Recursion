def fact(n):           # Question no:- 6
    if n == 0:
        return 1
    return n*fact(n-1)
print(fact(5))   