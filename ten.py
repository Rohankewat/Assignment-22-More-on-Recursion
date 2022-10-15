def printFibonacci(l1,count,a,b,n):  # Questin no :- 10
    if count != n:
        l1.append(a)
        a,b = b,a+b
        count += 1
        printFibonacci(l1,count,a,b,n)
    return l1[n-1]

print(printFibonacci([],0,0,1,10))      