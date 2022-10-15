def sumEvenN(n):             # Question no :- 3
    if n>1:
        return (n-2)+sumEvenN(n-2)
    return 0

print(sumEvenN(2*(1)+2))