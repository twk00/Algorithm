import sys

input = sys.stdin.readline

n = int(input())

def tile(n):
    dp = [0] * n 
    if n == 1:
        dp[0] = 1
    elif n == 2:
        dp[0] = 1
        dp[1] = 2
    else:
        dp[0] = 1
        dp[1] = 2
        dp[2] = 3
        for i in range(3,n):
            dp[i] = (dp[i-1] + dp[i-2])%15746
    return dp[-1]
print(tile(n))        