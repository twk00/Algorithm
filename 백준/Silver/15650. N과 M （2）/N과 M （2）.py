import sys

input = sys.stdin.readline

n,m = map(int, input().split())
list = []

def dfs(start):

    if len(list) == m:
        print(' '.join(map(str,list)))
        return
    
    for i in range(start,n+1):
        if i not in list:
            list.append(i)
            dfs(i+1)
            list.pop()

dfs(1)
