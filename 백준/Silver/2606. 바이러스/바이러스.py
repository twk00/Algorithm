import sys

sys.setrecursionlimit(10**6)
input = sys.stdin.readline
cnt = 0

n = int(input())
m = int(input())

graph = [[] for _ in range(n + 1)]
visit = [0] * (n + 1)
for _ in range(m):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)


def dfs(start):
    global cnt
    visit[start] = 1
    for i in graph[start]:
        if visit[i] == 0:
            visit[i] = 1
            cnt += 1
            dfs(i)


dfs(1)
print(cnt)
