import sys

input = sys.stdin.readline

n = int(input())

arr = list(map(int,input().split()))

def long(arr,n):
    dp = [1] * (n)

    for i in range(1,n):
        for j in range(0,i):
            if arr[i] > arr[j]:
                dp[i] = max(dp[i], dp[j] + 1)
    return max(dp)

print(long(arr,n))