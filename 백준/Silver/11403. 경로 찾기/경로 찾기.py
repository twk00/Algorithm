import sys
from collections import deque
input = sys.stdin.readline

n = int(input())
visit = [0] * n
graph = [list(map(int, input().split())) for _ in range(n)]
answer = [[0] * n for _ in range(n)]


for i in range(n):
    visit = [0] * n
    deq = deque([i])

    while deq:
        popnum = deq.popleft()
        for j in range(n):
            if graph[popnum][j] == 1 and visit[j] == 0:
                visit[j] = 1
                answer[i][j] = 1
                deq.append(j)

for j in answer:
    print(*j)

