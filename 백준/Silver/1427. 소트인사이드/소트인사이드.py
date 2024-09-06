import sys

input = sys.stdin.readline

n = input().rstrip()

list = []

for i in n:
    list.append(int(i))

list.sort(reverse=True)

for i in list:
    print(i,end='')
