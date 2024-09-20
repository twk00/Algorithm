import sys

input = sys.stdin.readline

days,window = map(int, input().split())
visit = list(map(int, input().split()))
check_visit = visit[0:window]
max_visit = sum(check_visit)
cnt = 1
current_sum = max_visit

for i in range(window, days):
    pop_num = check_visit.pop(0)
    check_visit.append(visit[i])
    current_sum = current_sum - pop_num + visit[i]

    if max_visit < current_sum:
        cnt = 1
        max_visit = current_sum
    elif max_visit == current_sum:
        cnt += 1

if max_visit == 0:
    print("SAD")
else:
    print(max_visit)
    print(cnt)

