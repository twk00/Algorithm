import sys
input = sys.stdin.readline

n = int(input())
egg = [list(map(int,input().split())) for _ in range(n)]
max_cnt = 0

def break_egg(start):
    global max_cnt

    if start == n: # 가장 오른쪽에 갔을 때
        cnt = 0
        for i in range(n): # 전체를 돌아서 
            if egg[i][0] <= 0: # 내구도가 0 이하면 
                cnt += 1  # 깨진 계란 갯수 추가
        max_cnt = max(max_cnt, cnt) # 최댓값 return
        return 
    
    if egg[start][0] <= 0: # 들고있는 계란이 깨졌을 때
        break_egg(start+1) # 시작했던 계란에서 오른쪽 한칸에서 시작
        return
    
    flag = True
    for i in range(n): 

        if i == start: # 본인 제외
            continue

        if egg[i][0] > 0: # 안깨짐
            flag = False
            break
        
    if flag: # 계란이 전부 깨져있을 경우
        max_cnt = max(max_cnt, n-1 ) # # 본인 빼고 최댓값 return
        return 
    
    for i in range(n):
        
        if i == start or egg[i][0] <= 0: # 들고 있는 계란이거나 깨져 있는 계란
            continue
        egg[start][0] -= egg[i][1] # 계란 치기
        egg[i][0] -= egg[start][1] # 치기 당한 계란
        break_egg(start + 1) # 두번 칠 수 없으니까 치고 백트래킹
        egg[start][0] += egg[i][1] # 원상복구
        egg[i][0] += egg[start][1] # 원상복구

break_egg(0)
print(max_cnt)