def sumN(n):             # Question no :- 1
    if n == 0:
        return 0
    return n+sumN(n-1)

print(sumN(5))