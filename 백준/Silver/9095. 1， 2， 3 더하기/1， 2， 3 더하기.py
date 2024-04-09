import sys

input = sys.stdin.readline

n = int(input())

def make(m):
    dp = [0] * (m)
    if m == 1:
        dp[0] = 1
    elif m == 2:
        dp[0] = 1
        dp[1] = 2
    else:
        dp[0] = 1
        dp[1] = 2
        dp[2] = 4

    for i in range(3,m):
        dp[i] = sum(dp[i-3:])

    return dp[-1]

for _ in range(n):
    
    m = int(input())
    print(make(m))