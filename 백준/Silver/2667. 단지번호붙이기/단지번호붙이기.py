import sys

sys.setrecursionlimit(10**6)
input = sys.stdin.readline
house = []
num = int(input())
cntarr = []
for _ in range(num):
    house.append(list(map(int, input().rstrip())))

cnt = 0


def dfs(x, y):
    global cnt
    if x <= -1 or x >= num or y <= -1 or y >= num:
        return False
    if house[x][y] == 1:
        cnt += 1
        house[x][y] = 0
        dfs(x - 1, y)
        dfs(x, y - 1)
        dfs(x, y + 1)
        dfs(x + 1, y)
        return True
    return False


result = 0
for i in range(num):
    for j in range(num):
        if dfs(i, j) == True:
            cntarr.append(cnt)
            cnt = 0
            result += 1
print(result)
cntarr.sort()
for i in cntarr:
    print(i)
