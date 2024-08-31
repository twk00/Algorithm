import sys
from collections import deque

input = sys.stdin.readline

a,b,c = map(int, input().split())

visited = [0] * (a+1)
graph = [[] for _ in range(a+1)]
answer = [0] * a
deq = deque([c])
cnt = 1

for _ in range(b):
    i,j = map(int, input().split())
    graph[i].append(j)
    graph[j].append(i)

for i in graph:
    i.sort()

while deq:
    popnum = deq.popleft()
    visited[popnum] = 1

    if answer[popnum-1] == 0:
        answer[popnum-1] = cnt
        cnt += 1

        for i in graph[popnum]:
            if visited[i] == 0:
                deq.append(i)

for i in answer:
    print(i)