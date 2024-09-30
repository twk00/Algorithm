import sys
input = sys.stdin.readline

n = int(input())

for i in range(n):
    answer = []
    data = list(map(int, input().split()))[1:]
    data.sort()
    print("Class", i+1)

    for j in range(len(data)-1):
        answer.append(data[j+1] - data[j])
    
    print('Max', str(max(data))+',',"Min",str(min(data))+",","Largest gap", max(answer))