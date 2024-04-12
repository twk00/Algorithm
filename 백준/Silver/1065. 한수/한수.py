import sys

input = sys.stdin.readline
 
n = int(input())
hansu = 0

for i in range(1,n+1):
    if i < 100:
        hansu  += 1
    if i >= 100:
        temp1 = int(str(i)[0]) - int(str(i)[1])
        temp2 = int(str(i)[1]) - int(str(i)[2])
        if temp1 == temp2:
            hansu += 1
print(hansu)