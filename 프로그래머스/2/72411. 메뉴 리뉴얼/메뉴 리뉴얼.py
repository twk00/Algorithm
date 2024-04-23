from itertools import combinations
def solution(orders, course):
    answer = []
    for i in course:
        dict = {}
        for j in orders:
            j_sort = sorted("".join(j))
            for k in combinations(j_sort,i):
                menu = "".join(k)
                
                if menu in dict:
                    dict[menu] += 1
                else:
                    dict[menu] = 1
                    
        for n,m in dict.items():
            if max(dict.values()) == m and m >= 2:
                answer.append(n)
    answer.sort()            
    return answer