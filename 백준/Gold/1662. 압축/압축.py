import sys
input = sys.stdin.readline

s = input().strip()
stack = []
before = ""
cnt = 0

for i in s:

    if i == "(":
        stack.append([cnt-1, before]) # k에서 1의 자리수 제외 => cnt -1
        cnt = 0 # 문자열 길이 측정 시작
    elif i == ")":
        popstr = stack.pop()
        cnt = cnt * int(popstr[1]) + popstr[0] # 압축 계산
    else:
        cnt += 1 # 문자열 길이 측정
        before = i # 1의 자리수 계산

print(cnt)

