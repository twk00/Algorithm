import sys
from collections import deque
input = sys.stdin.readline

dy = (-1,1,0,0,0,0)
dx = (0,0,-1,1,0,0)
dz = (0,0,0,0,-1,1)

def bfs(y,x,z):
    deq = deque()
    deq.append((y,x,z,0))

    while deq:
        ey,ex,ez,time = deq.popleft()

        for i in range(6):
            ny,nx,nz = ey + dy[i] , ex + dx[i] , ez + dz[i]

            if 0 <= ny < line and 0 <= nx < row and 0 <= nz < floor:
                if building[nz][ny][nx] == '.' and visit[nz][ny][nx] == 0:
                    visit[nz][ny][nx] = 1
                    deq.append((ny,nx,nz,time+1))
                elif building[nz][ny][nx] == "E" and visit[nz][ny][nx] == 0:
                    return f'Escaped in {time + 1} minute(s).'
    else:
        return "Trapped!"

while True:
    floor, line, row = map(int, input().split())

    if floor == 0 and line == 0 and row == 0:
        break

    building = []

    for _ in range(floor):
        building.append([list(map(str, input().strip())) for _ in range(line)])
        input()

    visit = [[[0] * row for _ in range(line)] for _ in range(floor)]

    for i in range(floor):
        for j in range(line):
            for k in range(row):
                if building[i][j][k] == "S":
                    visit[i][j][k] = 1
                    print(bfs(j,k,i))
                    break
