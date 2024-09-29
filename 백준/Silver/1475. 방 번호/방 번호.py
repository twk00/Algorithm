import sys

input = sys.stdin.readline

n = input().rstrip()
same = [0] * 10

for i in n:
    if i == "6" or i == "9":
        if same[6] == same[9]:
            same[6] += 1
        else:
            same[9] += 1
    else:
        same[int(i)] += 1

print(max(same))

