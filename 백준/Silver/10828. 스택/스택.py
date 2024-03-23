import sys

num = int(input())
arr = []
for _ in range(num):
    go = sys.stdin.readline().split()
    if go[0] == "push":
        arr.append(go[1])
    elif go[0] == "pop":
        if len(arr) == 0:
            print(-1)
        else:
            print(arr.pop())
    elif go[0] == "size":
        print(len(arr))
    elif go[0] == "empty":
        if len(arr) == 0:
            print(1)
        else:
            print(0)
    elif go[0] == "top":
        if len(arr) == 0:
            print(-1)
        else:
            print(arr[-1])