import sys

input = sys.stdin.readline

n,k = map(int, input().split())
weight = []
value = []

for _ in range(n):
    w,v = map(int, input().split())
    weight.append(w)
    value.append(v)

def knap(weight, value):
    dp = [[0] * (k+1) for _ in range(n+1)]

    for i in range(1, n+1):
        for j in range(1, k+1):
            if weight[i-1] > j:
                dp[i][j] = dp[i-1][j]
            else:
                dp[i][j] = max(dp[i-1][j], dp[i-1][j-weight[i-1]] + value[i-1])
    return dp[n][k]

print(knap(weight, value))