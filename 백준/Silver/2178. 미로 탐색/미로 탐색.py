import sys
from collections import deque

input = sys.stdin.readline

n,m = map(int,input().split())
graph=[]
deq = deque()
dx = (-1,1,0,0)
dy = (0,0,-1,1)

for _ in range(n):
    graph.append(list(int(i) for i in input().rstrip()))

def bfs(x,y):
    deq.append((x,y))
    while deq:
        x,y = deq.popleft()
        for i in range(4):
            nx = dx[i] + x
            ny = dy[i] + y
            if n> nx >= 0 and m > ny >= 0 and graph[nx][ny] == 1:
                graph[nx][ny] = graph[x][y] + 1
                deq.append((nx,ny))
    return graph[n-1][m-1]
print(bfs(0,0))
