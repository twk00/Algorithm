from collections import defaultdict
def solution(k, tangerine):
    answer = 0
    box = defaultdict(int)
    
    for i in tangerine:
        box[i] += 1
        
    sorted_box = sorted(box.values(), reverse=True)
    
    for i in sorted_box:
        k -= i
        answer += 1
        if k <= 0:
            break
    return answer