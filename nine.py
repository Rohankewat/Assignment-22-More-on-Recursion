def sumDigits(l1,n):       # Question no :- 7
    if n>0:
        r = n % 10
        n = n // 10
        l1.append(r)
        sumDigits(l1,n)
    return sum(l1)

print(sumDigits([],125))                        