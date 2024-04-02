import sys
from collections import deque

# 표준 입력에서 데이터를 읽어오는 함수를 직접 사용합니다.
input = sys.stdin.readline

t = int(input())
answer_ = []

def dfs(n, m, graph):
    visit = [0] * n
    for _ in range(m):
        i, j = map(int, input().split())
        graph[i - 1].append(j)
        graph[j - 1].append(i)
    for j in range(1, n + 1):
        if visit[j - 1] != 0:
            continue
        deq = deque([j])
        visit[j - 1] = 1
        result = "YES"
        while deq:
            popnum = deq.popleft()
            for i in graph[popnum - 1]:
                if visit[i - 1] == visit[popnum - 1]:
                    result = "NO"
                    break
                if visit[i - 1] == 0:
                    visit[i - 1] = 3 - visit[popnum - 1]
                    deq.append(i)
            if result == "NO":  # 만약 NO가 발견되면 루프를 종료합니다.
                break
        if result == "NO":  # 만약 NO가 발견되면 루프를 종료합니다.
            break
    return result

# 각 테스트 케이스에 대해 이분 그래프인지 확인한 결과를 저장합니다.
for _ in range(t):
    n, m = map(int, input().split())
    graph = [[] for _ in range(n)]
    answer_.append(dfs(n, m, graph))

# 모든 테스트 케이스에 대한 결과를 출력합니다.
for i in answer_:
    print(i)
