def find_receiving_towers(heights):
    receiving_towers = [0] * len(heights)
    stack = []  # 높이와 인덱스를 함께 저장할 스택

    for i, height in enumerate(heights):
        # 스택이 비어있지 않고, 스택의 탑이 현재 탑보다 높이가 낮다면
        while stack and heights[stack[-1]] <= height:
            stack.pop()  # 스택의 탑을 제거 (신호를 수신하는 탑이므로)

        # 스택이 비어있지 않다면, 스택의 탑이 신호를 수신하는 탑
        if stack:
            receiving_towers[i] = stack[-1] + 1  # 0이 아닌 1부터 시작하는 인덱스로 변환

        stack.append(i)  # 현재 탑의 인덱스를 스택에 추가

    return receiving_towers


# 입력 받기
N = int(input())  # 탑의 개수
heights = list(map(int, input().split()))  # 탑의 높이

# 결과 출력
result = find_receiving_towers(heights)
print(*result)
