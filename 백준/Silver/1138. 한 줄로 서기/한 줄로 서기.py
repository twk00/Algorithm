import sys
from collections import deque

input = sys.stdin.readline

n = int(input())

line = list(map(int, input().split()))
answer = [0] * n

for i in range(n):
    cnt = 0 

    for j in range(n):

        if cnt == line[i] and answer[j] == 0:
            answer[j] = i + 1
            break

        elif answer[j] == 0:
            cnt += 1

print(*answer)