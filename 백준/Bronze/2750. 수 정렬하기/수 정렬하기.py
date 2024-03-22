import sys

input = sys.stdin.readline
n = int(input())
c = []
for i in range(n):
    a = int(input())
    c.append(a)
set_list = set(c)
sort_list = sorted(set_list)
for i in sort_list:
    print(i)
