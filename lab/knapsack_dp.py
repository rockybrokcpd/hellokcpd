def knapSack(W, wt, val, n):
    dp = [0 for i in range(W+1)]  #dp array
  
    for i in range(1, n+1):  #first i elements
        for w in range(W, 0, -1):  # starting from back
            if wt[i-1] <= w:
                # find maximum value
                dp[w] = max(dp[w], dp[w-wt[i-1]]+val[i-1])
  
    return dp[W]  #max val return
val =[int(item) for item in input("Enter the profits: ").split()]
wt = [int(item) for item in input("Enter the weights: ").split()]
W = int(input("enter the capacity: "))
n = len(val)
print("max profit ="+str(knapSack(W, wt, val, n)))