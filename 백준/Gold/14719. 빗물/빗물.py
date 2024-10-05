import sys
input = sys.stdin.readline

h,w = map(int,input().split())
world = list(map(int, input().split()))
rain = 0

for i in range(1,w-1):
    left = max(world[:i]) # 좌측 제일 큰 높이 
    right = max(world[i+1:]) # 우측 제일 큰 높이
    small = min(left, right) # 그 중 더 작은 것 => 그래야 빗물 채울 수 있음

    if world[i] <= small : # 현재 높이가 small보다 작거나 같으면 빗물을 채울 수 있음
        rain += small - world[i] # 빗물 채우기

print(rain)





