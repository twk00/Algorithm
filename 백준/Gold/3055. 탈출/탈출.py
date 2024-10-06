import sys
from collections import deque

input = sys.stdin.readline

n, m = map(int, input().split())
graph = []
visit = [[-1] * m for _ in range(n)]
deq = deque()
dx = (-1, 1, 0, 0)
dy = (0, 0, -1, 1)

for _ in range(n):
    graph.append(list(map(str, input().strip())))

for i in range(n):
    for j in range(m):
        if graph[i][j] == "*":
            deq.appendleft((i, j)) 
        elif graph[i][j] == "S":
            deq.append((i, j))
            visit[i][j] = 0

result = -1 

while deq:
    x, y = deq.popleft()
    cur = graph[x][y]
    
    if cur == "S" and graph[x][y] == "D":
        result = visit[x][y]
        break
    
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if 0 <= nx < n and 0 <= ny < m:
            if visit[nx][ny] != -1:
                continue
            if graph[nx][ny] == "*":
                continue
            if graph[nx][ny] == "X":
                continue
            if cur == "*" and graph[nx][ny] == "D":
                continue
            if cur == "S":
                if graph[nx][ny] == "D":
                    result = visit[x][y] + 1
                    deq.clear() 
                    break
                visit[nx][ny] = visit[x][y] + 1
            graph[nx][ny] = cur
            deq.append((nx, ny))

if result != -1:
    print(result)
else:
    print("KAKTUS")