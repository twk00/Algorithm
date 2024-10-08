import sys
from itertools import combinations
input = sys.stdin.readline

n,l,r,x = map(int, input().split())
problems = list(map(int, input().split()))
answer = 0

for i in range(2, n+1):
    problem = list(combinations(problems, i))

    for j in problem:
        if l <= sum(j) <= r and max(j) - min(j) >= x:
            answer += 1
print(answer)