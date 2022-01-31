import sys
sys.stdin = open("sample_input1.txt", "r")

# 자기 방으로 돌아가기
# 수련회는 남에 방에서 자는게 국룰


# 1번방이나 2번방이나 복도 지나가는건 똑같아서 하나로 생각해줬다.
# 
# 400개의 방이지만 200개의 방으로 생각해주고 지나갈 복도의 개수를 카운팅해준다.
# 
# 구간이 겹치는 만큼 cnt 리스트의 요소 값이 커지므로 max 값을 출력하면 된다.
# 
# 이때 포인트는 항상 작은 숫자 방에서 큰 숫자 방으로만 움직이는게 아니기 때문에
# 
# for문을 돌면서 카운팅을 해주려면  작은숫자방-큰숫자방  이렇게 먼저 바꿔주고 순회해야 한다.

T = int(input())
for tc in range(1, T+1):
    N = int(input())  # 돌아가야할 학생수
    room_lst = [list(map(int, input().split())) for _ in range(N)]  # [[출발방, 도착방]]
    # print(room_lst)
    cnt = [0] * 201
    for room in room_lst:
        if room[0] < room[1]:
            s = (room[0] + 1) // 2
            e = (room[1] + 1) // 2
        else:
            e = (room[0] + 1) // 2
            s = (room[1] + 1) // 2

        #
        for j in range(s, e+1):
            cnt[j] += 1


    ans = max(cnt)

    print("#{} {}".format(tc, ans))



# 정성우

t = int(input())
for tc in range(t):
    n = int(input())
    v = [0] * n  # 방에 돌아갔는지 여부를 담아둘 배열
    mustgoback = []
    for _ in range(n):
        a, b = map(int, input().split())

        if a % 2:
            a = (a + 1) // 2
        else:
            a = a // 2
        if b % 2:
            b = (b + 1) // 2
        else:
            b = b // 2
        if a > b:  # 뒤의 조건식을 줄이기 위해서 숫자가 작은 것을 앞에 넣어준다
            a, b = b, a
        mustgoback.append((a, b))

    corridor = [0] * 401
    for start, end in mustgoback:
        for i in range(start, end + 1):
            corridor[i] += 1
    ans = 0

    for c in corridor:
        if c > ans:
            ans = c
    print(f'#{tc + 1}', ans)

