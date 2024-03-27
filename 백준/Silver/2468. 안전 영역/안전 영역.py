def dfs(x, y, height, visited):
    # 상, 하, 좌, 우 방향 벡터
    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]

    stack = [(x, y)]
    visited[x][y] = True

    while stack:
        curr_x, curr_y = stack.pop()

        # 상하좌우로 이동하면서 안전한 영역을 찾음
        for i in range(4):
            nx = curr_x + dx[i]
            ny = curr_y + dy[i]

            # 지도를 벗어나지 않고, 방문하지 않은 안전한 지점이면 스택에 추가
            if 0 <= nx < n and 0 <= ny < n and not visited[nx][ny] and area[nx][ny] > height:
                stack.append((nx, ny))
                visited[nx][ny] = True

# 지역의 크기 입력 받기
n = int(input())

# 지역의 높이 정보 입력 받기
area = [list(map(int, input().split())) for _ in range(n)]

# 결과값 초기화
result = 0

# 높이에 따라 잠기는 영역을 0부터 최대 높이까지 모두 확인
for height in range(max(map(max, area)) + 1):
    # 해당 높이에서 안전한 영역의 개수를 저장할 visited 배열 생성
    visited = [[False] * n for _ in range(n)]

    # 안전한 영역의 개수를 세기 위한 변수
    count = 0

    # 모든 지점을 돌면서 안전한 영역 개수 찾기
    for i in range(n):
        for j in range(n):
            if not visited[i][j] and area[i][j] > height:
                dfs(i, j, height, visited)
                count += 1

    # 현재 높이에서의 안전한 영역 개수가 최대인지 확인
    result = max(result, count)

# 결과 출력
print(result)
