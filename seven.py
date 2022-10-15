def printBin(n):       # Question no :- 8
    while n:
        print(bin(n))
        n = n-n
        printBin(n)
printBin(50)   