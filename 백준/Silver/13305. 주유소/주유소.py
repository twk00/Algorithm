import sys

input = sys.stdin.readline

city = int(input())

street = list(map(int, input().split()))
oil = list(map(int, input().split()))

price = street[0] * oil[0]

# for i in range(1, len(street)):
#     print(street[i],oil[i])

print(price + min(oil[1:-1]) * sum(street[1:]))