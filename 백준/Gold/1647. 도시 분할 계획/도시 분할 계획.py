import sys
from collections import deque
import heapq

input = sys.stdin.readline

n, m = map(int, input().split())
graph = [[] for _ in range(n)]
visit = [0] * (n+1)

for i in range(m):
    a, b, cost = map(int, input().split())
    graph[a-1].append((b, cost))
    graph[b-1].append((a, cost))

start_node = 0
visit[start_node] = 1
deq = [(cost, b) for b, cost in graph[start_node]]
heapq.heapify(deq)
total = []

while deq:
    cost, node = heapq.heappop(deq)
    if visit[node - 1] == 0:
        total.append(cost)
        visit[node - 1] = 1
        for b, c in graph[node - 1]:
            if visit[b - 1] == 0:
                heapq.heappush(deq, (c, b))
sorted_costs = sorted(total)

print(sum(sorted_costs[:-1]))