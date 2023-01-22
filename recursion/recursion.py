def printNos(n):
    if(n == 0):
        return
    printNos(n-1)
    print(n,end=" ")

def printGfg(n):
    if(n == 0):
        return
    printNos(n-1)
    print("GFG",end=" ")

def printRevNos(n):
    if(n == 0):
        return
    print(n,end=" ")
    printRevNos(n-1)

# printNos(10)
# printGfg(10)
# printRevNos(10)

