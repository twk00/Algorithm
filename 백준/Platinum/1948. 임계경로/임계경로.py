import sys
from collections import deque

input = sys.stdin.readline

N = int(input())   
M = int(input())   

time = [0] * (N+1)
in_degree = [0] * (N+1) 
graph = [[] for _ in range(N+1)]
cnt = [[] for _ in range(N+1)]

for _ in range(M):
    i, j, k = map(int, input().split())
    graph[i].append((k, j))
    in_degree[j] += 1

start, arrive = map(int, input().split())

que = deque([])
que.append(start)

while que:
    popnum = que.popleft()
    # cost: 비용, des: 도시
    for i in graph[popnum]:
        cost = i[0]
        des = i[1]
        in_degree[des] -= 1
        # 비용이 갱신 될 때
        if time[des] < time[popnum] + cost:
            time[des] = time[popnum] + cost
            # 달려야 하는 도로의 수 갱신
            cnt[des] = [popnum]
        elif time[des] == time[popnum] + cost:
            cnt[des].append(popnum)

        # 선행 도로를 모두 지나갔을 때
        if in_degree[des] == 0:
            que.append(des)

deq = deque([arrive])
route = set()

while deq:
    popnum = deq.popleft()
    for x in cnt[popnum]:
        if (popnum, x) not in route:
            route.add((popnum, x))
            deq.append(x)

print(time[arrive])
print(len(route))