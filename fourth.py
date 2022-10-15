def sqSum(n):               #  Question no :- 4
    if n>0:
        return (n**2)+sqSum(n-1)
    return 0
print(sqSum(5))