import sys
from collections import deque

input = sys.stdin.readline

ladder_cnt,snake_cnt = map(int, input().split())
ladders = dict()
snakes = dict()
visit = [False] * 101
board = [0] * 101

for _ in range(ladder_cnt):
    i,j = map(int, input().split())
    ladders[i] = j

for _ in range(snake_cnt):
    i,j = map(int, input().split())
    snakes[i] = j

def bfs(start):
    deq = deque([start])
    visit[start] = True

    while deq:
        current = deq.popleft()

        for i in range(1,7):
            move = current + i
            
            if 0 < move <= 100 and visit[move] == False:
                if move in ladders:
                    move = ladders[move]

                if move in snakes:
                    move = snakes[move]

                if visit[move] == False:
                    deq.append(move)
                    visit[move] = True
                    board[move] = board[current] + 1

bfs(1)
print(board[100])