import sys
import itertools
input = sys.stdin.readline

n , sum1 = map(int, input().split())
arr = list(map(int, input().split()))
cnt = 0
for i in range(1,n+1):
    new = itertools.combinations(arr,i)
    sum_arr = 0
    for j in new:
        sum_arr =  sum(j)
        if sum_arr == sum1:
            cnt += 1
        
print(cnt)