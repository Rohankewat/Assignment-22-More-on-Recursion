def sqSum(n):               #  Question no :- 5
    if n>0:
        return (n**3)+sqSum(n-1)
    return 0
print(sqSum(5))