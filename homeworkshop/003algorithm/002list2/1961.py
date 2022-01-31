import sys
sys.stdin = open("input.txt", "r")

# 90도 회전 arr[-1-r][c], 아래에서 위로 읽어내는 방법
# 180도 회전 arr[-1-r][-1-c], 오른쪽에서 왼쪽으로 읽는 방법
# 270도 회전 arr[r][-1-c], 위에서 아래로 읽되, 오른쪽부터

T = int(input())
# print(T)
for test_case in range(1, T + 1):
    N = int(input())
    # 2차원 리스트로 받기
    arr = [input().split() for _ in range(N)]
    # print(arr)
    ans = [] # 첫 열// 둘째 열// 셋째 열

    # 90도 첫 열
    result = []  # 빈리스트 갱신
    for c in range(N):
        # 빈문자열
        data = ''
        for r in range(N):
            data += arr[-1-r][c]
        result.append(data)
    ans.append(result)
    # print(ans)

    # 180도 둘째 열
    result = []  # 빈리스트 갱신
    for r in range(N):
        data = ''
        for c in range(N):
            data += arr[-1-r][-1-c]
        result.append(data)
    ans.append(result)
    # print(ans)

    # 270도 셋째 열
    result = []  # 빈리스트 갱신
    for c in range(N):
        data = ''
        for r in range(N):
            data += arr[r][-1-c]
        result.append(data)
    ans.append(result)
    # print(ans)

    # 출력 # 출력이 너무 어려운데
    print('#{}'.format(test_case))
    for i in range(N):
        print(ans[0][i], ans[1][i], ans[2][i])
        # print(ans[0][i])
        # print(ans[1][i])
        # print(ans[2][i])


def rotate(origin):
    N = len(origin)
    rotated = [[0] * N for _ in range(N)]
    for y in range(N):
        for x in range(N):
            rotated[x][y] = origin[N - 1 - y][x]
    return rotated


# 문찬솔

# 테스트 케이스 입력
T = int(input())
# 테스트 케이스 만큼 수행
for tc in range(1, T + 1):
    # NxN 행렬의 N 입력
    N = int(input())
    # 처음 행렬을 담을 변수 선언
    basic = []
    for _ in range(N):
        basic.append(list(map(int, input().split(" "))))

    # 90도 회전
    r90 = rotate(basic)
    # 180도 회전
    r180 = rotate(r90)
    # 270도 회전
    r270 = rotate(r180)

    # 출력 시작
    print('#{}'.format(tc))
    for i in range(N):
        # unpacking 활용
        print(*r90[i], sep='', end=' ')
        print(*r180[i], sep='', end=' ')
        print(*r270[i], sep='', end=' ')
        print()