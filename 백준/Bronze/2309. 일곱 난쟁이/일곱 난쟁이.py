import sys

input = sys.stdin.readline
a = [int(input()) for _ in range(9)]
sum = sum(a)
a = sorted(a)
b= 0
c=0
result = []
for i in range(9):
    for j in range(i+1,9):
        if sum - (a[i] + a[j]) == 100:
            c = a[i]
            b = a[j]
            break
for i in a:
    if i != c and i!= b:
        print(i)



    