from collections import deque
import sys

input = sys.stdin.readline

n, m = map(int, input().split())
miro = []
dx = (-1, 1, 0, 0)
dy = (0, 0, -1, 1)

for _ in range(n):
    miro.append(list(map(int, input().rstrip())))


def bfs(x, y):
    deq = deque()
    deq.append((x, y))
    while deq:
        x, y = deq.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < n and 0 <= ny < m and miro[nx][ny] == 1:
                deq.append((nx, ny))
                miro[nx][ny] = miro[x][y] + 1
    return miro[n - 1][m - 1]


print(bfs(0, 0))
