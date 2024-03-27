import sys
from collections import deque

input = sys.stdin.readline
a,b = map(int, input().split())
que = deque([i for i in range(1,a+1)])
answer = []

arr = [ i for i in range(1,a+1)]
cnt = 0
while cnt <= a:
    c = 0
    for _ in range(b):
        c += 1
        if len(que) == 0:
            break
        if c == b:
            answer.append(str(que.popleft()))
        else:
            que.append(que.popleft())
    cnt += 1
print("<", ", ".join(answer), ">", sep="")

    




