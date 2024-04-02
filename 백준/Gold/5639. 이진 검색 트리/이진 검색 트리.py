import sys
from collections import deque

input = sys.stdin.readline
sys.setrecursionlimit(10**6)
arr = []

while True:
    try:
        n = int(input())
        arr.append(n)
    except:
        break

def bin(arr):

    if len(arr) == 0:
        return
    
    left,right = [],[]

    mid = arr[0]

    for i in range(1, len(arr)):
        if arr[i] > mid:
            left = arr[1:i]
            right = arr[i:]
            break
    else:
        left = arr[1:]
    
    bin(left)
    bin(right)
    print(mid)
    
bin(arr)