import sys

input = sys.stdin.readline

n,m = map(int, input().split())

days = []
pages = []

for _ in range(m):
    i,j = map(int, input().split())
    days.append(i)
    pages.append(j)

def day6(days, pages):
    dp = [[0] * (n+1) for _ in range(m+1)]

    for i in range(1, m+1):
        for j in range(1, n+1):
            if j < days[i-1]:
                dp[i][j] = dp[i-1][j]
            else:
                dp[i][j] = max(dp[i-1][j], dp[i-1][j - days[i-1]] + pages[i-1])
    return dp[m][n]

print(day6(days, pages))