import sys

sys.setrecursionlimit(10**6)
input = sys.stdin.readline

num = int(input())
house = []
answer = []
cnt = 0
total = 0

for _ in range(num):
    house.append(list(map(int, input().rstrip())))

def dfs (x,y):
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

for i in range(num):
    for j in range(num):
        if dfs(i,j) == True:
            answer.append(cnt)
            cnt = 0
            total += 1

answer.sort()
print(total)
for i in answer:
    print(i)