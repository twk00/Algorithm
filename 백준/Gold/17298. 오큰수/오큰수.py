import sys

input = sys.stdin.readline

n = int(input())
list = list(map(int, input().split()))
answer = [-1] * n
stack = [0]

for i in range(1,n):
    while stack and list[stack[-1]] < list[i]:
        answer[stack.pop()] = list[i]
    stack.append(i)
print(*answer)