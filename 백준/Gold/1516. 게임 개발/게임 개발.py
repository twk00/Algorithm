import sys
from collections import deque
input = sys.stdin.readline

n = int(input())
game = [[] for _ in range(n + 1)]
inDegree = [0] * (n + 1)
time = [0] * (n + 1)
result = [0] * (n + 1)

for i in range(1, n + 1):
    info = list(map(int, input().split()))
    time[i] = info[0]
    for j in info[1:-1]:
        game[j].append(i)
        inDegree[i] += 1

def dp_sort():
    deq = deque()
    
    for i in range(1, n + 1):
        if inDegree[i] == 0:
            deq.append(i)
            result[i] = time[i]
    
    while deq:
        now = deq.popleft()
        for i in game[now]:
            inDegree[i] -= 1
            result[i] = max(result[i], result[now] + time[i])
            if inDegree[i] == 0:
                deq.append(i)

dp_sort()

for i in range(1, n + 1):
    print(result[i])