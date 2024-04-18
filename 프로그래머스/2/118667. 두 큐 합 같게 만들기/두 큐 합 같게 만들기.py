from collections import deque
def solution(queue1, queue2):
    answer = 0
    deq1 = deque(queue1)
    deq2 = deque(queue2)
    total1 = sum(deq1)
    total2 = sum(deq2)
    sumtotal = total1 + total2
    size = len(deq1) * 3
    
    if sumtotal % 2 != 0:
        return -1
    
    while True:
        if total1 > total2:
            num = deq1.popleft()
            deq2.append(num)
            total1 -= num
            total2 += num
            answer += 1
        elif total2 > total1:
            num = deq2.popleft()
            deq1.append(num)
            total1 += num
            total2 -= num
            answer += 1
        else:
            break
        
        if answer == size:
            answer = -1
            break
            
        
    return answer