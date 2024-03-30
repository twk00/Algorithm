from collections import deque
import sys

input = sys.stdin.readline
n = int(input())
graph = [[] for _ in range(n+1)]
deq = deque([1])
visited = [0] * (n+1)
answer = [0] * (n-1)
for _ in range(n-1):
    i,j = map(int, input().split())
    graph[i].append(j)
    graph[j].append(i)

while deq:
    popnum = deq.popleft()
    visited[popnum] = 1
    for i in graph[popnum]:
        if visited[i] == 0:
            deq.append(i)
            answer[i-2] = popnum
for i in answer:
    print(i)
