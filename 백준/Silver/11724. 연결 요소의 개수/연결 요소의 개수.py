import sys
from collections import deque

input = sys.stdin.readline
sys.setrecursionlimit(10**6)

# n,m = map(int, input().split())
# graph = [(0,0) for _ in range(m)]
# parent = [0] * (n + 1)
# deq = deque()
# result = 0
# def find(parent,x):
#     if parent[x] == x:
#         return x
#     parent[x] = find(parent, parent[x])
#     return parent[x]

# def union(parent,a,b):
#     rootA = find(parent,a)
#     rootB = find(parent,b)

#     if rootA < rootB:
#         parent[rootB] = rootA
#     else:
#         parent[rootA] = rootB
# for k in range(m):
#     i,j = map(int, input().split())
#     graph[k] = (i,j)

# for i in range(1, n + 1):
#     parent[i] = i

# for i in graph:
#     a,b = i
#     if find(parent,a) != find(parent,b):
#         union(parent,a,b)
# for i, v in enumerate(parent):
#     if i == v:
#         result += 1
# print(result -1)


n,m = map(int, input().split())
graph = [[]for _ in range(n+1)]
visit = [0] * (n+1)
answer = 0

def dfs(node):
    deq = deque([node])
    deq.append(node)
    visit[node] = 1
    while deq:
        popnum = deq.pop()
        for i in graph[popnum]:
            if visit[i] == 0:
                visit[i] = 1
                deq.append(i)

for _ in range(m):
    i,j = map(int,input().split())
    graph[i].append(j)
    graph[j].append(i)


for i in range(1,n+1):    
    if not visit[i]:
        dfs(i)
        answer += 1

print(answer)

# n, m = map(int, input().split())
# graph = [[] for _ in range(n + 1)]
# visit = [0] * (n + 1)
# answer = 0

# def dfs(node):
#     visit[node] = 1
#     for neighbor in graph[node]:
#         if not visit[neighbor]:
#             dfs(neighbor)

# for _ in range(m):
#     i, j = map(int, input().split())
#     graph[i].append(j)
#     graph[j].append(i)

# for i in range(1, n + 1):
#     if not visit[i]:
#         dfs(i)
#         answer += 1

# print(answer)
            