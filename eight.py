def printOct(n):       # Question no :- 9
    while n:
        print(oct(n))
        n = n-n
        printOct(n)
printOct(1)   