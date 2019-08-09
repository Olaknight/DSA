#Using dynamic programming (Mamoisation)

def fibo(n):
    myDict = {}
    if n == 1 or n == 2:
        return 1

    if n in myDict:
        return myDict[n]

    else:
        myDict[n] = fibo(n - 1) + fibo(n - 2)
        return myDict[n]


print(fibo(10))