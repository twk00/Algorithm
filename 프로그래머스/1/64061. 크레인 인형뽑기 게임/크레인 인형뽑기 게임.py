def solution(board, moves):
    answer = 0
    collect = []
    for i in moves:
        for j in range(len(board)):
            if board[j][i-1] != 0:
                collect.append(board[j][i-1])
                board[j][i-1] = 0
                break
        
        if len(collect) > 1 and collect[-1] == collect[-2]:
            answer += 2
            collect = collect[:len(collect)-2]
    
    return answer