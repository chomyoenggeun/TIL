# import sys
#
# sys.stdin = open("input.txt", "r")
#
# for tc in range(1, 2):
#     T = int(input())
#     ladder = [list(map(int, input().split())) for _ in range(100)]
#     print(ladder)

import sys

sys.stdin = open("input.txt", "r")

# 문제 접근 방법 1. 답부터 찾고 푼다. 한방에 시작점을 찾는다.
# 문제 접근 방법 2. 반복문을 통해 첫 시작을 잡는다.

# 1번 방법 도착점부터 찾기

# 상 우 좌 = 위 오 왼, 델타를 이용한 2차원 접근방법
dr = [-1, 0, 0]
dc = [0, 1, -1]

T = 10
for test_case in range(1, T + 1):
    t = int(input())
    # 왜? 벽에서 왼쪽 오른쪽으로 못갔을 경우를 대비
    # 양 끝에 벽을 세워주기 위해 0 컬럼 추가  # 여기서 헤맴
    a = [[0] + list(map(int, input().split())) + [0] for _ in range(100)]

    # c: 도착점 column idx 구하기
    for j in range(102):
        if a[99][j] == 2:
            c = j

    # 방향 위로 초기화
    d = 0  # 0: 위, 1: 오, 2: 왼
    r = 99
    while True:  # 반복문 무한루프
        # 반복문 계속 돌리다가 row 인덱스가 0 이 되면 끝내고 리턴
        if r == 0: # 종료조건
            break

        # 왼쪽에 1이 있으면 왼쪽으로 계속 가다가 0 나오면 반복문 종료
        if a[r][c - 1]:
            d = 2
            while True:
                r += dr[d]     # 왼쪽
                c += dc[d]
                if a[r][c - 1] == 0:
                    break

        # 오른쪽에 1이 있으면 오른쪽으로 계속 가다가 0 나오면 반복문 종료
        elif a[r][c + 1]:
            d = 1
            while True:
                r += dr[d]     # 오른쪽
                c += dc[d]
                if a[r][c + 1] == 0:
                    break

        # 양옆에 1 하나도 없으면 계속 직진(i.e. d=0) 또는
        # 왼쪽이든 오른쪽이든 가다가 next col에서 0이면 d=0(위)로 체인지
        d = 0
        r += dr[d]       # 위로
        c += dc[d]

    print("#{} {}".format(test_case, c - 1)) # 벽때문에 인덱스 -1





# 2번 방법 같은말

T = 10
for test_case in range(1, 11):
    # for test_case in range(1, T+1):
    N = 100
    num = int(input())

    arr = [list(map(int, input().split())) for _ in range(N)]

    # 2인 값, 도착지점을 찾는다
    goal = 0  # 도착지점 초기화
    for col in range(100):
        if arr[99][col] == 2:  # 인덱스 도착행중에 2값을 찾으면
            goal = col  # 도착지점의 열 인덱스
            break  # break 생각지도 못했다....

    c = goal  # c좌표, 열
    step = 98  # r좌표, 행

    # 시작지점 찾기
    while step > 0:  # 0이되면 종료, 행이 0이 되면 종료
        right = left = True  # 종료조건만들기   # 여기도 어려움
        if c - 1 < 0:  # 좌
            right = True
            left = False
        elif c + 1 > 99:  # 우
            left = True
            right = False

        # 왼쪽과 오른쪽 길이 있다면 방향 전환
        if left and arr[step][c - 1]:
            c -= 1
            while not arr[step - 1][c]:
                c -= 1
        elif right and arr[step][c + 1]:
            c += 1
            while not arr[step - 1][c]:
                c += 1


    print("#{} {}".format(num, c))



# 성아영

for tc in range(1, 11):
    T = int(input())
    ladder = [list(map(int, input().split())) for _ in range(100)]

    # 아래로 가는 경우는 고려안함
    dx = [0, -1, 1]
    dy = [-1, 0, 0]

    cur_pos_x = 0
    for i in range(100):
        if ladder[99][i] == 2:
            cur_pos_x = i
            break
    cur_pos_y = 99
    while cur_pos_y > 0:
        for idx in range(3):
            temp_x = cur_pos_x + dx[idx]
            temp_y = cur_pos_y + dy[idx]
            if 0 <= temp_x < 100 and 0 <= temp_y < 100 and ladder[temp_y][temp_x]:
                cur_pos_x = temp_x
                cur_pos_y = temp_y

                # 이미 방문한 지점은 값을 바꿔줌
                ladder[temp_y][temp_x] = 0
                continue
    print("#{} {}".format(tc, cur_pos_x))



# 강동옥

for _ in range(1, 11):
    tc = int(input())
    ladder = [[int(i) for i in input().split()] for _ in range(100)]

    for idx, val in enumerate(ladder[-1]):
        if val == 2:
            c = idx
            break

    r = 99

    while r > 0:
        if 0 <= c - 1 < 100 and ladder[r][c - 1]:
            ladder[r][c] = 0
            c -= 1
        elif 0 <= c + 1 < 100 and ladder[r][c + 1]:
            ladder[r][c] = 0
            c += 1
        else:
            r -= 1

    print('#{} {}'.format(tc, c))



# 박준영

dr = [0, 0, -1]  # 우 좌 상
dc = [1, -1, 0]

for tc in range(1, 11):
    T = int(input())
    Ladder = [list(map(int, input().split())) for _ in range(100)]
    d = 0
    r = 0
    c = 0
    ans_i = 0  # 출발 지점
    for i in range(100):  # 100 번 반복하는데  거꾸로 시작
        if Ladder[99][i] == 2:  # 마지막행  i 번째가 2 이라면
            r = 99  # 행좌표 99
            c = i  # 열좌표
            now = 0  # 현재 상태
    while r != 0:  # 행이 100이 될때까지 반복
        if 0 <= r + dr[0] < 100 and 0 <= c + dc[0] < 100:  # 오른쪽으로 움직일때 벽을 만나지 않으면서
            if Ladder[r + dr[0]][c + dc[0]] == 1 and now != 1:  # 오른쪽옆이 1이고 현재상태가 1(왼쪽으로움직이는게 아닐때)
                r, c = r + dr[0], c + dc[0]  # 그방향으로 진행하고
                now = 2  # 현재상태 2
                continue
        if 0 <= r + dr[1] < 100 and 0 <= c + dc[1] < 100:  # 왼쪽으로 움직일때 벽을 만나지 않으면서
            if Ladder[r + dr[1]][c + dc[1]] == 1 and now != 2:  # 왼쪽옆이 1이고 현재상태가 2(오른쪽으로 움직이는게 아닐때)
                r, c = r + dr[1], c + dc[1]  # 그방향으로 진행하고
                now = 1  # 현재상태 1
                continue
        r, c = r + dr[2], c + dc[2]  # 둘다 아니면 위로 한칸
        now = 0  # 현재상태 0

    ans_i = c  # 현재출발 지점



# 문찬솔

for _ in range(10):
    T = int(input())
    ladder = [list(map(int, input().split())) for _ in range(100)]

    r = 99
    c = 0
    dr = [-1, 0, 0]  # 상, 좌, 우
    dc = [0, -1, 1]
    d = 0
    for i in range(100):
        if ladder[r][i] == 2:
            c = i
            break
    while r:
        if d != 2 and c > 0 and ladder[r][c - 1]:
            d = 1
        elif d != 1 and c < 99 and ladder[r][c + 1]:
            d = 2
        else:
            d = 0
        r += dr[d]
        c += dc[d]

    print("#{} {}".format(T, c))


# 양지훈

def buy_icecream():
    for t in range(10):
        tc = int(input())
        arr = [[0] + list(map(int, input().split())) + [0] for _ in range(100)]
        idx_2 = 0
        for find in range(101):
            if arr[99][find] == 2:
                idx_2 = find

        i, j = 99, idx_2
        while i > 0:
            if arr[i][j - 1] == 1:
                while arr[i][j - 1] == 1:
                    j -= 1
            elif arr[i][j + 1] == 1:
                while arr[i][j + 1] == 1:
                    j += 1
            i -= 1
        print("#{} {}".format(tc, j - 1))


buy_icecream()