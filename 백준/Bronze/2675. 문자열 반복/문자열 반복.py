import sys

input = sys.stdin.readline
n = int(input())
answer = []
for _ in range(n):
    a,b = map(str,input().rstrip().split())
    c = ""
    for i in b:
        c = c + i*int(a)
    answer.append(c)
for i in answer:
    print(i)