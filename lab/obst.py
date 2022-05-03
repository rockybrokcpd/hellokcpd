def optCost(fre, i, j):
    if j < i:
        return 0
    if j == i:
        return fre[i]
    fsum = Sum(fre, i, j)
    Min = 999
    for r in range(i, j + 1):
        cost = (optCost(fre, i, r - 1) +optCost(fre, r + 1, j))
        if cost < Min:
            Min = cost
    return Min + fsum
def optimalSearchTree(keys, fre, n):
    return optCost(fre, 0, n - 1)
def Sum(fre, i, j):
    s = 0
    for k in range(i, j + 1):
        s += fre[k]
    return s
if __name__ == '__main__':
    keys=[]
    fre=[]
    keys = [int(item) for item in input("Enter the keys: ").split()]
    fre = [int(item) for item in input("Enter the fre: ").split()]
    n = len(keys)
    print("Cost of OBST is",optimalSearchTree(keys, fre, n))