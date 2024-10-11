import sys
input = sys.stdin.readline

N = int(input())
stack = []
total_score = 0

for _ in range(N):
    task = list(map(int, input().split()))
    
    if task[0] == 1:
        stack.append([task[1], task[2]])
    
    if stack:
        stack[-1][1] -= 1
        
        if stack[-1][1] == 0:
            score, _ = stack.pop()
            total_score += score

print(total_score)