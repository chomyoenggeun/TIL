# # 색칠하기


# 1번방식

T = int(input())

for test_case in range(1, T+1):
    n = int(input())
    arr = [[0 for _ in range(11)] for a in range(11)]  # 좌표평면 10개짜리 이차원 리스트 받기 어렵네, _ a 변수 사용 별로네

    cnt = 0    # 보라영역의 갯수 초기화
    for i in range(n):
        # 좌표평면 받기
        r1, c1, r2, c2, color = map(int, input().split())
        # x와 y 좌표평면을 모두 나타낸다
        for x in range(r1, r2 + 1):
            for y in range(c1, c2 + 1):
                #  해당 좌표 평면에 color 점수를 더한다. 점수를 통해서 구분
                arr[x][y] += color
                # 그 중 합이 3인것이 보라색 영역이다.
                if arr[x][y] == 3:
                    cnt += 1

    print("#{} {}".format(test_case, cnt))



# 2번 방식
T = int(input())

for test_case in range(1, T+1):
    N = int(input())
    redarea = [] # 레드 영역
    bluearea = [] # 블루 영역

    for i in range(N):
        y1, x1, y2, x2, color = map(int, input().split()) # y, x 좌표와 색깔을 map으로 list형식으로 받는다
        # 좌표평면의 범위 설정
        for y in range (y1, y2+1): # range범위때문에 +1   # 여기서 막힘
            for x in range(x1, x2+1):
                if color == 1: #조건문
                    redarea.append((y, x))   # 레드 영역, 리스트
                elif color == 2:
                    bluearea.append((y, x)) # 블루 영역, 리스트

        purple = []  # 결과값을 빈리스트로 만든후 답은 len으로 갯수값 반환

    if len(redarea) > len(bluearea):  # 레드 영역이 블루영역보다 크면
        for j in bluearea:  # 블루 영역 중
            if j in redarea: # 레드 영역에 블루 영역이 있으면
                purple.append(j)   # 추가한다.

    if len(redarea) < len(bluearea): # 블루영역이 레드영역보다 크다면
        for j in redarea:  # 레드 영역 중
            if j in bluearea:   # 블루 영역에 레드 영역이 있으면
                purple.append(j)  # 추가한다.


    print("#{} {}".format(test_case, len(purple)))


# 박수아

T = int(input())

for tc in range(1, T+1):
    arr = [[0] * 10 for _ in range(10)]
    num = int(input())
    ans = 0
    for draw in range(num):
        color = list(map(int,input().split()))
        for i in range(color[0], color[2]+1):
            for j in range(color[1], color[3]+1):
                if arr[i][j] != 0 and arr[i][j] != color[4]:
                    arr[i][j] = 3
                    ans += 1
                else:
                    arr[i][j] = color[4]
    print('#{} {}'.format(tc, ans))

