import sys
sys.stdin = open("input3.txt", "r")

def max_max(max_num):
    if max_num < total:
        max_num = total
    return max_num

T = int(input())

for tc in range(1, T+1):
    arr = [list(map(int, input().split())) for _ in range(100)]
    # print(arr)

    total = 0
    max_num = 0

    # 행 확인
    for i in range(100):
        total = 0  # 초기화
        for j in range(100):
            total += arr[i][j]
        max_max(max_num)

    # 열 확인

    for i in range(100):
        total = 0  # 초기화
        for j in range(100):
            total += arr[j][i]
        max_max(max_num)

    # 대각확인
    for i in range(len(arr)):
        total = 0  # 초기화
        for i in range(len(arr)):
            total += arr[i][i]
        max_max(max_num)

    total = 0
    for i in range(100):
        for j in range(100):
            total += arr[i][100-1-i]
        max_max(max_num)

    print("#{} {}".format(tc, max_num))


