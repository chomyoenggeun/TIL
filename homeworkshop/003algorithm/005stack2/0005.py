arr = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

r = 1
c = 1
N = 3

# 상하좌우
dr = [-1, 1, 0, 0]
dc = [0, 0, -1, 1]

# 위에거랑 같다
drc = [[-1, 0], [1, 0], [0, -1], [0, 1]]
# di, dj, | dx, dy | dy, dx

for i in range(4):
    # nr = r + dr[i]
    # nc = c + dc[i]
    nr = r + drc[i][0]
    nc = c + drc[i][1]

    # for dr, dc in ([-1, 0], [1, 0], [0, -1], [0, 1])

    # 범위 안에 들어와 있을 떄 아래의 코드를 실행해 주세요
    # if 0 <= nr < N and 0 <= nc < N:
    #     print(arr[nr][nc], end = " ")

    # 범위 안에 들어오지 않았다면 그냥 다음 차례로 넘겨주세요
    # if nr < 0 or nr >= N or nc < 0 or nc >= N:
    #     continue
    # print(arr[nr][nc], end = " ")

    # 첫 번째, 에러안남
    if 0 <= nr < N and 0 <= nc < N and arr[nr][nc] == 2:
        print("오 2있네")
    # 두 번째, 에러남
    if arr[nr][nc] == 2 and 0 <= nr < N and 0 <= nc < N:
        print("오 2있네")

# 전치행렬



