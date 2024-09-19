import sys
import heapq as hq

input = sys.stdin.readline

n,m = map(int, input().split())

gifts = []
state = True

for i in list(map(int, input().split())):
    hq.heappush(gifts, -i)

children = list(map(int, input().split()))

for i in children:
    gift = -hq.heappop(gifts)
    if gift < i:
        state = False
        break
    hq.heappush(gifts, -(gift-i))

if state:
    print(1)
else:
    print(0)