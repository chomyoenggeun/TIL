import sys
sys.stdin = open("input3.txt", "r")

def check():
    for i in range(9):
        # 체크를 위한
        row = [0] * 10
        col = [0] * 10

        for j in range(9):
            # 행을 검사
            num_row = sudoku[i][j]
            # 열을 검사
            num_col = sudoku[j][i]

            # 이미 사용한 숫자라면 너 멈춰
            if row[num_row]:
                return 0
            if col[num_col]:
                return 0

            row[num_row] = 1
            col[num_col] = 1

            # 3X3 검사도 한번에
            if i % 3 == 0 and j % 3 == 0:
                square = [0] * 10

                for r in range(i, i+3):
                    for c in range(j, j+3):
                        num = sudoku[r][c]
                        # 중복된 숫자가 나온다면 그만
                        if square[num]:
                            return 0
                        square[num] = 1
    return 1

T = int(input())

for tc in range(1, T+1):
    sudoku = [list(map(int, input().split())) for _ in range(9)]

    print("#{} {}".format(tc, check()))








def check():
    for i in range(9):
        # 체크를 위한
        row = [0] * 10
        col = [0] * 10

        for j in range(9):
            # 행을 검사
            num_row = sudoku[i][j]
            # 열을 검사
            num_col = sudoku[j][i]

            # 이미 사용한 숫자라면 멈춰
            if row[num_row]:
                return 0
            if col[num_col]:
                return 0

            row[num_row] = 1
            col[num_col] = 1

            # 3X3 검사도 한번에 처리를 해버리자
            if i % 3 == 0 and j % 3 == 0:
                square = [0] * 10

                for r in range(i, i+3):
                    for c in range(j, j+3):
                        num = sudoku[r][c]
                        # 중복된 숫자가 나온다면 그만
                        if square[num]:
                            return 0
                        square[num] = 1

    return 1

T = int(input())

for tc in range(1, T+1):
    sudoku = [list(map(int, input().split())) for _ in range(9)]

    print("#{} {}".format(tc, check()))





# 스도쿠의 개념
# 가로 확인, 세로 확인, 사각형 확인


# 1번
# T = int(input())
#
# for test_case in range(1, T+1):
    # 1차원 리스트로 받기
    # arr = list(map(int, input().split()))
    # print(arr)

# # 2번
# T = int(input())
#
# for test_case in range(1, T+1):
#     # print(test_case)
#     # 2차원 리스트로 받기
#     arr = [list(map(int, input().split())) for _ in range(10)]
#     # print(arr) # 10번째는 왜 못받지? # 10개가 아니네?ㅋㅋㅋ






T = int(input())

def check(arr):
    # 가로 확인
    for i in range(9):
        # 빈리스트를 만들어서 숫자를 넣는다
        check = []
        # 9x9의 행렬을 확인
        for j in range(9):
            if check:
                if arr[i][j] in check:
                    return '0'
            check.append(arr[i][j])

    # 세로 확인
    for i in range(9):
        check = []
        for j in range(9):
            if check:
                if arr[j][i] in check:
                    return '0'
            check.append(arr[j][i])

    # 블록 확인 # 여기가 어려움 # 9칸을 비교
    for i in range(0, 9, 3):  # 시작점
        for j in range(0, 9, 3):
            check = []

            # 블록
            for k in range(3):
                for t in range(3):
                    if check:
                        if arr[i + k][j + t] in check:
                            return '0'
                    check.append(arr[i + k][j + t])
    return '1' # 다 맞으면 1을 반환


for tc in range(1, T + 1):
    arr = [list(map(int, input().split())) for _ in range(9)]
    print("#{}".format(tc), end=' ')
    print(check(arr))





#
# # 이승훈
#
# T = int(input())
# for _ in range(T):
#     N = [[0] * 9 for __ in range(9)]
#     for n in range(9):
#         N[n] = list(map(int, input().split()))
#     cube = [0] * 10
#     for k in range(3):
#         for l in range(3):
#             cube[N[k][l]] += 1
#     if cube != [0, 1, 1, 1, 1, 1, 1, 1, 1, 1]:
#         print(f'#{_ + 1} 0')
#         continue
#     for i in range(9):
#         galo = [0] * 10
#         selo = [0] * 10
#         for j in range(9):
#             galo[N[i][j]] += 1
#             selo[N[j][i]] += 1
#
#         if galo != [0, 1, 1, 1, 1, 1, 1, 1, 1, 1] or selo != [0, 1, 1, 1, 1, 1, 1, 1, 1, 1]:
#             print(f'#{_ + 1} 0')
#             break
#
#     else:
#         print(f'#{_ + 1} 1')
#


# 전호정

# 스도쿠 검증
# 합 구하는 함수
# def mySum(arg):
#     total = 0
#     for s in range(len(arg)):
#         total += arg[s]
#     return total
#
#
# T = int(input())
# for tc in range(1, T + 1):
#
#     # 2차원 리스트 입력
#     num = []
#     for i in range(9):
#         num.append(list(map(int, input().split())))
#
#     c_list = []  # num의 행과 열을 바꾼 리스트
#     b_list = []  # 구역 리스트로 이루어진 리스트
#     ans = 1  # 출력값 1로 초기화 -> 탈출문에 걸리면 0으로 갱신
#
#     # 열 체크
#     for i in range(9):
#         c_list = []
#         for j in range(9):  # 열 고정 행 순회
#             c_list.append(num[j][i])  # 세로줄 (열)의 리스트 만들기
#         if mySum(list(set(c_list))) != 45:  # 중복을 제거한 후 합이 45가 아니면
#             ans = 0  # 출력값 0으로 갱신후
#             break  # 반복문 탈출
#
#     # 구역 체크
#     for i in range(3):
#         for j in range(3):  # 구역별 중복 확인 후 합 확인
#             if mySum(list(set([num[3 * i][3 * j], num[3 * i + 1][3 * j], num[3 * i + 2][3 * j], num[3 * i][3 * j + 1],
#                                num[3 * i][3 * j + 2], num[3 * i + 1][3 * j + 1], num[3 * i + 1][3 * j + 2],
#                                num[3 * i + 2][3 * j + 1], num[3 * i + 2][3 * j + 2]]))) != 45:
#                 ans = 0
#                 break
#
#     # 행 체크
#     for i in range(9):
#         if mySum(list(set(num[i]))) != 45:
#             ans = 0
#             break
#
#     print('#{} {}'.format(tc, ans))