import sys

input = sys.stdin.readline

n = int(input().strip())

distances = list(map(int, input().strip().split()))

prices = list(map(int, input().strip().split()))

min_cost = 0
min_price = prices[0]

for i in range(n - 1):
    if prices[i] < min_price:
        min_price = prices[i]
    min_cost += min_price * distances[i]

print(min_cost)
