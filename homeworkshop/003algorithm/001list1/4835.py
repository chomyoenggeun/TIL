T = int(input()) # test_case 갯수

for test_case in range(1, T+1):
    N, M = map(int, input().split())    # N은 정수 갯수, M은 구간
    num = list(map(int, input().split()))


    max_sum = 0
    min_sum = 987654321   # 임의의 큰값
    result = 0            # 결과값 초기화
    for i in range(N-M+1):  # 구간만큼 앞까지 돈다
        sum_num = 0   # 구간합      # 요개 안에 있어야댐 멍청아
        for j in range(M):  # 구간만큼 보자
            sum_num += num[i+j]  # 구간 안의 합
        if sum_num > max_sum:
            max_sum = sum_num  # 최대합 구간 갱신
        if sum_num < min_sum:
            min_sum = sum_num  # 최소합 구간 갱신

    result = max_sum - min_sum

    print("#{0} {1}".format(test_case, result))

