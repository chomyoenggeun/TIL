# 교수님 답

T = int(input())

for tc in range(1, T+1):
    # 박스의 수
    N = int(input())
    box = list(map(int, input().split())) #입력 받음..

    ans = 0

    #전체 모든 박스 비교
    for i in range(N):
        cnt = 0

        #나 다음부터 나보다 작은 값을 찾아 카운트 하자
        for j in range(i+1, N):
            if box[i] > box[j]:
                cnt += 1

        if ans < cnt:
            ans = cnt
    print("#{} {}".format(tc, ans))


# 내꺼 안됨
T = int(input())
for test_case in range(1, T+1):   # test_case 갯수
    N = int(input())    # 리스트 길이
    a = list(map(int, input().split()))  # 리스트 내용

    for i in range(N-1, 0 , -1):      # 뒤에서 부터 쌓을 건데
        for j in range(0, i):        # 길이는 점점 줄어들면서 볼거다
            if a[j] > a[j+1]:    # 앞의 값이 뒤의 값보다 크다면
                a[j], a[j+1] = a[j+1], a[j]        # 자리를 바꿔라

    print("#{0} {1}".format(test_case, a))
