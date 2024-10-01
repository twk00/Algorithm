import sys
input = sys.stdin.readline

n,k = map(int, input().split())
coin = []
dp = [0] * (k+1)
dp[0] = 1 # 기본값으로 초기화

for _ in range(n):
    coin.append(int(input()))

for i in coin:
    for j in range(i, k+1):
        dp[j] += dp[j - i] # 점화식

print(dp[k])
    
