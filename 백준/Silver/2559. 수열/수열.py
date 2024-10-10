import sys
input = sys.stdin.readline

n, k = map(int, input().split())
arr = list(map(int, input().split()))

answer = sum(arr[:k])
cur = answer

for i in range(n - k):

    cur = cur - arr[i] + arr[i + k]
    answer = max(answer, cur)

print(answer)