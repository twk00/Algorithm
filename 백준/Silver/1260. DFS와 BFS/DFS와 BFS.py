from collections import deque
import sys

input = sys.stdin.readline

a, b, c = map(int, input().split())

graph = [[] for _ in range(a + 1)]
visited_dfs = [0] * (a + 1)
visited_bfs = [0] * (a + 1)
answer_dfs = []
answer_bfs = []
deq = deque([c])

for _ in range(b):
    i, j = map(int, input().split())
    graph[i].append(j)
    graph[j].append(i)


def dfs():
    for i in graph:
        i.sort(reverse=True)
    while deq:
        popnum = deq.pop()
        visited_dfs[popnum] = 1
        if popnum not in answer_dfs:
            answer_dfs.append(popnum)
            for i in graph[popnum]:
                if visited_dfs[i] == 0:
                    deq.append(i)
    print(" ".join(map(str, answer_dfs)))


def bfs():
    for i in graph:
        i.sort()
    while deq:
        popnum = deq.popleft()
        visited_bfs[popnum] = 1
        if popnum not in answer_bfs:
            answer_bfs.append(popnum)
            for i in graph[popnum]:
                if visited_bfs[i] == 0:
                    deq.append(i)
    print(" ".join(map(str, answer_bfs)))


dfs()
deq.clear()
deq.append(c)
bfs()
