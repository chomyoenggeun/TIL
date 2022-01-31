import sys
sys.stdin = open("input.txt", "r")

# 띄를 만들자

T = int(input())

for tc in range(1, T+1):
    # N : 2차원리스트 크기, K : 내가 찾고 싶은 길이
    N, K = map(int, input().split())

    # 띄를 만들자
    puzzle = [list(map(int, input().split())) + [0] for _ in range(N)]
    puzzle.append([0] * (N+1))

    ans = 0

    for i in range(N):
        # 행을 검사
        cnt_r = 0
        for j in range(N+1):
            if puzzle[i][j] == 1: # 흰색부분
                cnt_r += 1
            else:
                # 벽이라면
                if cnt_r == K:
                    ans += 1
                cnt_r = 0

        # 열을 검사
        cnt_c = 0
        for j in range(N+1):
            if puzzle[j][i] == 1:
                cnt_c += 1
            else:
                if cnt_c == K:
                    ans += 1
                cnt_c = 0

    print("#{} {}".format(tc, ans))






# 띄없이

T = int(input())

for tc in range(1, T+1):
    # N : 2차원리스트 크기, K : 내가 찾고 싶은 길이
    N, K = map(int, input().split())

    puzzle = [list(map(int, input().split())) for _ in range(N)]
    ans = 0

    for i in range(N):
        # 행 검사
        cnt_r = 0
        for j in range(N):
            if puzzle[i][j] == 1: #흰색부분이야
                cnt_r += 1
            else:
                # 벽이라면
                if cnt_r == K:
                    ans += 1
                cnt_r = 0

        # 열 검사
        cnt_c = 0
        for j in range(N):
            if puzzle[j][i] == 1:
                cnt_c += 1
            else:
                if cnt_c == K:
                    ans += 1
                cnt_c = 0

        if cnt_c == K:
            ans += 1

    print("#{} {}".format(tc, ans))











# 어디에 단어가 들어갈 수 있을까
# 접근방법 : 단어가 들어가는 1을 count하고 K단어길이와 맞는걸 찾는다.


T = int(input()) # tc_ 갯수받기

for tc in range(1, T+1):
    # 각각 N: 2차원 리스트 크기(가로 세로), K: 단어길이
    N, K = map(int, input().split())

    #리스트 내포 방식을 활용한 입력
    puzzle = [list(map(int, input().split())) for _ in range(N)]
    # print(puzzle)
    ans = 0 # 결과값 0으로 초기화

    for i in range(N):
        cnt = 0   # 초기화 중요!!! # 고생함
        # 행을 검사
        for j in range(N):
            if puzzle[i][j] == 1:
                cnt += 1
            if puzzle[i][j] == 0 or j == N-1:
                # 벽을 만났을 때 그동안 쌇아온 cnt 값이 k(단어의 길이)이면 들어갈 수 있다.
                if cnt == K:
                    ans += 1
                cnt = 0

        # 열을 검사
        for j in range(N):
            if puzzle[j][i] == 1:
                cnt += 1
            if puzzle[j][i] == 0 or j == N-1:
                if cnt == K:
                    ans += 1
                cnt = 0

    print("#{} {}".format(tc, ans))


