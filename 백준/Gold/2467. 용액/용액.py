import sys

input = sys.stdin.readline

n = int(input())  
liquid = list(map(int, input().split())) 

start = 0
end = n - 1
zero_liquid = 2000000000
answer = [0,0]  

while start < end:
    mixed_liquid = liquid[start] + liquid[end]
    
    if abs(mixed_liquid) <= abs(zero_liquid):
        zero_liquid = mixed_liquid
        answer = [liquid[start], liquid[end]] 
    
    if mixed_liquid == 0:
        break
    
    if mixed_liquid < 0:
        start += 1
    else:
        end -= 1

print(answer[0], answer[1])
