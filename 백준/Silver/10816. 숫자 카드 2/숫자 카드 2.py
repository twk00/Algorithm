import sys
input = sys.stdin.readline

def lower(arr, target):
    left, right = 0, len(arr)
    while left < right:
        mid = (left + right) // 2
        if arr[mid] >= target:
            right = mid
        else:
            left = mid + 1
    return left

def upper(arr, target):
    left, right = 0, len(arr)
    while left < right:
        mid = (left + right) // 2
        if arr[mid] > target:
            right = mid
        else:
            left = mid + 1
    return left

n = int(input())
card = sorted(list(map(int, input().split())))
m = int(input())
cnt = list(map(int, input().split()))

result = []
for i in cnt:
    low = lower(card, i)
    up = upper(card, i)
    result.append(up - low)

print(' '.join(map(str, result)))