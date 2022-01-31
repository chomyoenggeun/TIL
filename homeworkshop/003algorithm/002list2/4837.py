# 부분집합의 합

T = int(input())

for test_case in range(1, T+1):
    N, K = map(int, input().split()) # N은 원소 수 # K는 원소합
    # A = [int(i) for i in range(1, 13)]  # 여기서 너무 막혔음
    A = list(range(1, 13)) # 1~ 12 집합 A

    cnt = 0

    for i in range(1<<len(A)): # 부분집합 생성
        subset = []   # 원소 수를 리스트로 구현   # 여기서도 막힘
        A_sum = 0    # 원소 합을 리스트로 구현X  # 여기서 너무 막힘
        for j in range(len(A)):
            if i & (1<<j):
                subset.append(A[j])
                A_sum += A[j]   # 리스트를 합으로 나타냄
        #부분집합 원소 갯수가 N이면서, 원소 합이 K이면 +1
        if len(subset) == N and A_sum == K:  # sum이 리스트이면 K정수와 비교 불가능
            cnt += 1

    print("#{} {}".format(test_case, cnt))




# 박준영
# 부분집합의 합
data = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]  # 12까지의 숫자
list_data = []  # 부분집합 배열
n = len(data)  # data 의 개수
for i in range(1 << n):  # n 번 쉬프트
    list_d = []  # 각 부분집합의 리스트
    for j in range(n):  # n 번반복
        if i & (1 << j):  # 1을 j 번 쉬프트
            list_d.append(data[j])  # 부분집합을 저장
    list_data.append(list_d)  # 그부분집합을 전부 저장

T = int(input())  # 케이스 수
for tc in range(1, T + 1):
    cnt = 0  # 존재하는 부분집합의 수
    N, K = map(int, input().split())  # N 개  K 합
    for d in list_data:  # 부분집합중
        sum_data = 0
        if len(d) == N:  # 길이가 N 이고
            for num in d:  # 그 합이
                sum_data += num
            if sum_data == K:  # K 이면
                cnt += 1  # 1 증가

    print('#{} {}'.format(tc, cnt))



# 강동옥
# 12486. 4837. [파이썬 S/W 문제해결 기본] 2일차 - 부분집합의 합

T = int(input())
for tc in range(1, T + 1):
    N, K = map(int, input().split())
    A = list(range(1, 13))
    cnt = 0
    for i in range(1 << 12):
        nn = 0  # 부분집합의 수

        for n in str(bin(i))[2:]:
            nn += int(n)  # 부분집합의 수

        if nn == N:  # 부분집합의 수 == N일때
            part = []
            part_sum = 0
            for j in range(12):
                if i & 1 << j:
                    part.append(A[j])

            for num in part:
                part_sum += num

            if part_sum == K:  # 합이 K일때
                cnt += 1

    print('#{} {}'.format(tc, cnt))