import sys
sys.stdin = open("input1.txt", "r")


# # 이동좌표 1번방법
# dx = [0, 1, -1, 0] # 오 하 상 왼  # 우 하 상 좌
# dy = [1, 0, 0, -1]

# 이동좌표 리스트로 만드는 법

move = [(0, 1), (1, 0), (-1, 0), (0, -1)] # 우 하 상 좌

# 아 미로랑 정점 간선은 좀 차이나네
def dfs(x, y):
    global ans
    # 목표점 도착 or 결과가 이미 나왔다면 리턴
    if maze[x][y] == 3 or ans:
        ans = 1 # 가능하다
        return

    for i, j in move:
        dx = x + i
        dy = y + j
        # 반복돌리다 결과 나오면 리턴
        if ans:
            return
        # 벽이 아니거나 제자리가 아니면
        elif maze[dx][dy] != 1:
            # 현재위치를 벽으로 체크하고 재귀
            maze[x][y] = 1
            dfs(dx, dy)


T = 10
# print(T)
for tc in range(1, T+1):
    num = int(input())
    # 리스트내포방식 : 2차원 리스트 만들기
    maze = [list(map(int, input())) for _ in range(16)]
    # print(maze)

    ans = 0  # 결과값 초기화 # 1은 가능하다 # 0은 불가능하다

    # 출발점 찾기
    x, y = 0, 0 # 요거 개념이 맨날 헷갈림, x 행 y 열 # 내가 아는 좌표랑 헷갈려ㅠㅠ
    for i in range(16):
        for j in range(16):
            if maze[i][j] == 2: # 출발점 2
                x, y = i, j
    # print(x, y)

    # DFS로 미로 찾기
    # 출발값부터 탐색시작
    dfs(x, y)

    print("#{} {}".format(tc, ans))







# # # 이동좌표 1번방법
# # dx = [0, 1, -1, 0] # 오 하 상 왼  # 우 하 상 좌
# # dy = [1, 0, 0, -1]
#
# # 이동좌표 리스트로 만드는 법
#
# move = [(1, 0), (-1, 0), (0, 1), (0, -1)]
#
# # 아 미로랑 정점 간선은 좀 차이나네
# def dfs(y, x):
#     global ans
#     # 목표점 도착 or 결과가 이미 나왔다면 리턴
#     if maze[y][x] == 3 or ans:
#         ans = 1  # 가능하다
#         return
#
#     for i, j in move:
#         dy = y + i
#         dx = x + j
#         # 반복돌리다 결과 나오면 리턴
#         if ans:
#             return
#         # 벽이 아니거나 제자리로 왔다면
#         elif maze[dy][dx] != 1:
#             # 현재위치를 벽으로 체크하고 재귀
#             maze[y][x] = 1
#             dfs(dy, dx)
#
#
# T = 10
# # print(T)
# for tc in range(1, T + 1):
#     num = int(input())
#     # 리스트내포방식 : 2차원 리스트 만들기
#     maze = [list(map(int, input())) for _ in range(16)]
#     # print(maze)
#
#     ans = 0  # 결과값 초기화 # 1은 가능하다 # 0은 불가능하다
#
#     # 출발점 1, 1
#
#     dfs(1, 1)
#
#     print("#{} {}".format(num, ans))




