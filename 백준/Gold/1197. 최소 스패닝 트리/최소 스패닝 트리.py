import sys

input = sys.stdin.readline

v, e = map(int, input().split())
graph = [(0, 0, 10000) for _ in range(e)]
parent = [0] * (v + 1)
result = 0

for k in range(e):
    i, j, cost = map(int, input().split())
    graph[k] = (i, j, cost)

def heap(graph):
    n = len(graph)
    for i in range(n // 2 - 1, -1, -1):
        make_heap(graph, n, i)
    for i in range(n - 1, 0, -1):
        graph[i], graph[0] = graph[0], graph[i]
        make_heap(graph, i, 0)
    return graph

def make_heap(arr, n, i):
    parent = i
    left = i * 2 + 1
    right = i * 2 + 2
    if left < n and arr[left][2] > arr[parent][2]:
        parent = left
    if right < n and arr[right][2] > arr[parent][2]:
        parent = right
    if parent != i:
        arr[parent], arr[i] = arr[i], arr[parent]
        make_heap(arr, n, parent)

def find(parent, x):
    if parent[x] == x:
        return x
    parent[x] = find(parent, parent[x])
    return parent[x]

def union(parent, a, b):
    rootA = find(parent, a)
    rootB = find(parent, b)

    if rootA < rootB:
        parent[rootB] = rootA
    else:
        parent[rootA] = rootB

heap(graph)

for i in range(1, v + 1):
    parent[i] = i

for i in graph:
    a, b, cost = i
    if find(parent, a) != find(parent, b):
        union(parent, a, b)
        result += cost
print(result)

# import sys

# input = sys.stdin.readline

# v, e = map(int, input().split())
# graph = []  # graph 리스트를 빈 리스트로 초기화
# parent = [0] * (v + 1)
# result = 0

# for k in range(e):
#     i, j, cost = map(int, input().split())
#     graph.append((i, j, cost))  # graph 리스트에 간선 정보를 추가

# # 간선의 가중치를 기준으로 오름차순으로 정렬
# graph.sort(key=lambda x: x[2])
# print(graph)
# def find(parent, x):
#     if parent[x] == x:
#         return x
#     parent[x] = find(parent, parent[x])
#     return parent[x]

# def union(parent, a, b):
#     rootA = find(parent, a)
#     rootB = find(parent, b)

#     if rootA < rootB:
#         parent[rootB] = rootA
#     else:
#         parent[rootA] = rootB

# # 부모 테이블상에서, 부모를 자기 자신으로 초기화
# for i in range(1, v + 1):
#     parent[i] = i

# # Kruskal 알고리즘 수행
# for edge in graph:
#     a, b, cost = edge
#     if find(parent, a) != find(parent, b):
#         union(parent, a, b)
#         result += cost

# print(result)

