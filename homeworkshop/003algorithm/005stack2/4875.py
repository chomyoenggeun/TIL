import sys
sys.stdin = open("sample_input.txt", "r")



# 미로

def is_Safe(x, y):
    return 0 <= x < N and 0 <= y < N and (maze[x][y] == 0 or maze[x][y] ==3)



def dfs(x, y):
    global ans
    # 목표점 도착 or 결과가 이미 나왔다면 리턴
    if maze[x][y] == 3 or ans:
        ans = 1  # 가능하다
        return

    visited.append((x, y))

    for i in range(4): # 방향
        new_x = x + dx[i]
        new_y = y + dy[i]

        if is_Safe(new_x, new_y) and (new_x, new_y) not in visited:
            dfs(new_x, new_y)


T = int(input().strip())

for tc in range(1, T+1):
    N = int(input()) # NxN 가로세로길이
    maze = [list(map(int, input().strip() )) for _ in range(N)]
    # print(maze)
    # 출발점 찾기
    x, y = 0, 0  # x 행 y 열
    for i in range(N):
        for j in range(N):
            if maze[i][j] == 2:  # 출발점 2
                x, y = i, j
    # print(x, y)

    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]

    ans = 0
    visited = []

    # DFS로 미로 찾기
    # 출발값부터 탐색시작
    dfs(x, y)
    print("#{} {}".format(tc, ans))








# 성아영

for tc in range(int(input())):
    size = int(input())
    maze = [[1] * (size + 2)]
    for _ in range(size):
        maze.append([1] + list(map(int, input().strip())) + [1])
    maze.append([1] * (size + 2))
    stack = []
    start_idx = (0, 0)
    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]
    for i in range(size + 2):
        for j in range(size + 2):
            if maze[i][j] == 2:
                start_idx = (i, j)
                maze[i][j] = 0

    result = 0
    stack.append(start_idx)
    while stack:
        cur = stack.pop()
        if maze[cur[0]][cur[1]]:
            continue
        maze[cur[0]][cur[1]] = 1

        for idx in range(4):
            tmp_x = cur[1] + dx[idx]
            tmp_y = cur[0] + dy[idx]
            if maze[tmp_y][tmp_x] == 0:
                stack.append((tmp_y, tmp_x))
            elif maze[tmp_y][tmp_x] == 3:
                result = 1
                break
    print("#{} {}".format(tc + 1, result))



