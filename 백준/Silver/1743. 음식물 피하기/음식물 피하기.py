import sys
from collections import deque

input = sys.stdin.readline

n, m, k = map(int, input().split())  
graph = [[0 for _ in range(m)] for _ in range(n)]
visit = [[0 for _ in range(m)] for _ in range(n)]

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

for _ in range(k):
    y, x = map(int, input().split())
    graph[y - 1][x - 1] = 1  

def bfs(start_x, start_y):
    queue = deque()
    queue.append((start_x, start_y))
    visit[start_x][start_y] = 1  
    area_size = 1  

    while queue:
        x, y = queue.popleft()

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if 0 <= nx < n and 0 <= ny < m and graph[nx][ny] == 1 and not visit[nx][ny]:
                queue.append((nx, ny))
                visit[nx][ny] = 1
                area_size += 1

    return area_size

max_size = 0
for i in range(n):
    for j in range(m):
        if graph[i][j] == 1 and not visit[i][j]:  
            max_size = max(max_size, bfs(i, j))

print(max_size)
