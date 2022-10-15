def sumOddN(n):             # Question no :- 2
    if n>0:
        return (n-2)+sumOddN(n-2)
    return 1
print(sumOddN(2*(1)+1))