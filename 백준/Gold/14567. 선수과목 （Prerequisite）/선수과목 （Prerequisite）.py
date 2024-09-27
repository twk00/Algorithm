import sys
from collections import deque

input = sys.stdin.readline

n, m = map(int, input().split())
graph = [[] for _ in range(n+1)]
in_degree = [0] * (n+1)
semester = [0] * (n+1)

for _ in range(m):
    a, b = map(int, input().split())
    graph[a].append(b)
    in_degree[b] += 1

def topology_sort():
    queue = deque()
    
    for i in range(1, n+1):
        if in_degree[i] == 0:
            queue.append(i)
            semester[i] = 1

    while queue:
        current = queue.popleft()

        for next_course in graph[current]:
            in_degree[next_course] -= 1
            if in_degree[next_course] == 0:
                queue.append(next_course)
                semester[next_course] = semester[current] + 1

topology_sort()
print(*semester[1:])
