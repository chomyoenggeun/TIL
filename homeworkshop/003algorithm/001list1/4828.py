# 1번 방법
T = int(input()) # test_case 갯수

for test_case in range(1, T+1):
    N = int(input())    # 받는 정수 갯수
    nums = list(map(int, input().split()))  # 리스트받기

    max_num = nums[0]  # 최대값
    min_num = nums[0]  # 최소값

    for num in nums:  # 정수값들을 for문으로 비교하겠다.
        if num > max_num:
            max_num = num  # 최댓값 갱신

        if num < min_num:
            min_num = num  # 최솟값 갱신
    result = max_num - min_num
    print("#{0} {1}".format(test_case, result))






# 2번 방법 - 왜 안되냐??
T = int(input()) # test_case 갯수

for test_case in range(1, T+1):
    N = int(input())    # 받는 정수 갯수
    num = list(map(int, input().split()))  # 리스트받기

    max_num = num[0]  # 최대값
    min_num = num[0]  # 최소값
    for i in range(N):      # i는 인덱스를 순차적으로 보겠다
        for j in range(N-1):  # j는 i다음 인덱스를 보겠다.
            if num[i] > num[j+1]:
                max_num = num[i]

            if num[i] < num[j+1]:
                min_num = num[i]
        result = max_num - min_num
    print("#{0} {1}".format(test_case, result))




# 교수님 방법

T = int(input()) # test_case 갯수

for test_case in range(1, T+1):
    N = int(input())    # 받는 정수 갯수
    nums = list(map(int, input().split()))  # 리스트받기












    # 박신영 - 버블정렬로 풀기

T = int(input()) # test_case 갯수

for i in range(1, T+1):
    N = int(input())  # 받는 정수 갯수
    nums = list(map(int, input().split()))   # 리스트 받기

    result = ''

    for j in range(N-1, 0, -1):  # 리스트 마지막 구간까지 보겠다.
        for k in range(j):       # 버블정렬이용
            if nums[k] > nums[k+1]:       # 앞의 값이 뒤의 값보다 크면
                nums[k], nums[k+1] = nums[k+1], nums[k]  # 앞 뒤 값 교환

            result = nums[-1] - nums[0]    # 정렬을 이용해 Max -Min 을 구한다.

    print('#{0} {1}'.format(i, result))
