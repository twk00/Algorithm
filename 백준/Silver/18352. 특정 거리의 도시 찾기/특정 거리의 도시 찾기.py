import sys
from collections import deque
input = sys.stdin.readline
n,m,k,x = map(int, input().split())
graph = [[] for _ in range(n)]
visit = [0] * n
cnt = 0
deq = deque()
answers = []
deq.append((x,0))
visit[x-1] = 1
for _ in range(m):
    i,j = map(int, input().split())
    graph[i-1].append(j)

while deq:
    popnum,cnt_total = deq.popleft()
    
    if cnt_total  == k:
        answers.append(popnum)
    
    for i in graph[popnum-1]:
        if visit[i-1] == 0:
            visit[i-1] = 1
            deq.append((i,cnt_total+1))

if not answers:
    print(-1)
else:    
    answers.sort()
    for i in answers:
        print(i)