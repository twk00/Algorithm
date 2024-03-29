from collections import deque
import sys

input = sys.stdin.readline

n,m = map(int, input().split())
graph = [[]for _ in range(n+1)]
visited = [0] * (n+1)
deq = deque()
answer = []
for _ in range(m):
    a,b = map(int, input().split())
    graph[a].append(b)
    visited[b] += 1

for i in range(1,n+1):
    if visited[i] == 0:
        deq.append(i)

while deq:
    popnum = deq.popleft()
    answer.append(popnum)
    for i in graph[popnum]:
        visited[i] -= 1
        if visited[i] == 0:
            deq.append(i)
print(*answer)
