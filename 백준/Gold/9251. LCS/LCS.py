import sys

input = sys.stdin.readline

a = input().rstrip()
b = input().rstrip()

def lcs(a, b):
    a = "-" + a
    b = "-" + b
    
    dp = [[0] * len(b) for _ in range(len(a))]

    for y in range(1,len(a)):
        for x in range(1,len(b)):
            if a[y] == b[x]:
                dp[y][x] = max(dp[y-1][x], dp[y][x-1], dp[y-1][x-1] + 1)
            else:
                dp[y][x] = max(dp[y-1][x],dp[y][x-1])

    return dp[-1][-1]

print(lcs(a,b))