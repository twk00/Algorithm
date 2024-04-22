from collections import deque

def solution(record):
    answer = []
    que = deque([])
    info = {}
    
    for i in record:
        spl = i.split()
        if spl[0] == 'Enter':
            que.append((spl[1], 0))
        elif spl[0] == 'Leave':
            que.append((spl[1], 1))
        if spl[0] == 'Enter' or spl[0] == 'Change':
            info[spl[1]] = spl[2]
    
    while que:
        uid, now = que.popleft()
        if not now:
            answer.append(f"{info[uid]}님이 들어왔습니다.")
        else:
            answer.append(f"{info[uid]}님이 나갔습니다.")
            
    return answer