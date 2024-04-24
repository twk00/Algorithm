import sys

input = sys.stdin.readline

n = int(input().strip())
person = []

for _ in range(n):
    a, b = map(int, input().split())
    person.append([a,b]) 

for i in person: 
    rank = 1
    for j in person: 
        if i[0] < j[0] and i[1] < j[1]:
            rank += 1
    print(rank, end=' ')