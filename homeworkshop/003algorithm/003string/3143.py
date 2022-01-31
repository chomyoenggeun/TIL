import sys
sys.stdin = open("sample_input3.txt", "r")


def nums():
    idx = 0
    cnt = 0
# b가 들어갈 수 있는지 확인하기
# 조건 - 확인할 수 있는 길이가 b의 길이만큼 존재해야 한다.
    while idx < a_len - b_len + 1: # 인덱스 길이가 a길이 b길이보다 작아야한다
        if a[idx:idx + b_len] == b:  # 인덱스값에 대한 같은지 비교
            cnt += 1 # 같으면 카운트
            idx += b_len # 인덱스길이도 b길이만큼 더해준다
        else:
            cnt += 1 
            idx += 1

    # 남은 글자 처리하기 # a길이와 비교
    while idx < a_len:
        cnt += 1
        idx += 1

    return cnt


T = int(input())
for tc in range(1, T+1):
    a, b = map(str, input().split())

    a_len = len(a)
    b_len = len(b)

    print('#{} {}'.format(tc, nums()))



T = int(input())
for tc in range(1, T+1):
    a, b = map(str, input().split())

    a_len = len(a)
    b_len = len(b)

    idx = 0
    cnt = 0
    # b가 들어갈 수 있는지 확인하기
    # 조건 - 확인할 수 있는 길이가 b의 길이만큼 존재해야 한다.
    while idx < a_len - b_len + 1:  # 인덱스 길이가 a길이 b길이보다 작아야한다
        if a[idx:idx + b_len] == b:  # 인덱스값에 대한 같은지 비교
            cnt += 1  # 같으면 카운트
            idx += b_len  # 인덱스길이도 b길이만큼 더해준다
        else:
            cnt += 1
            idx += 1

    # 남은 글자 처리하기 # a길이와 비교
    while idx < a_len:
        cnt += 1
        idx += 1

    result = cnt

    print('#{} {}'.format(tc, result))






# 정성우

t = int(input())
for tc in range(t):
    a, b = input().split()
    n = len(a)
    m = len(b)
    ans = n
    i = 0
    while i < n:
        if a[i:i + m] == b:
            ans -= m - 1
            i += len(b) - 1
        i += 1

    print(f'#{tc + 1} {ans}')


# 김도훈

T = int(input())
for tc in range(T):
    a, b = map(str, input().split())
    idx = 0  # 인덱스
    cnt = 0  # 입력 횟수

    while True:
        # 인덱스가 마지막까지 도달하면 종료
        if idx == len(a):
            break

        # 해당 인덱스에서 b크기만큼 슬라이싱 했을 때 b랑 같으면 횟수 1로 추가하고 길이만큼 인덱스 넘어간다.
        if a[idx:idx + len(b)] == b:
            idx += len(b)
            cnt += 1
        # 아닐경우 입력횟수 +1, 인덱스 +1
        else:
            idx += 1
            cnt += 1

    print("#{} {}".format(tc + 1, cnt))



fr test_case in range(1, T+1):for tc in range(1,1+T):
    a,b = map(str,input().split())

    a_len = len(a)
    b_len = len(b)

    res = find()

    print('#{} {}'.format(tc,res))
    print(str1)
    print(str2)
    # count를 쓴다면
    ans = len(str1) - (len(str2) - 1) * str1.count(str2)
    # print(ans)
    print("#{} {}".format(test_case, ans))

    # # 방법 1 안쓴다면? what should I do same effect?
    N = len(str1)
    M = len(str2)
    cnt = 0
    ans = 0
    for i in range(N):
        if str1[i:i+M] == str2:  # 인덱스 값이 넘어가 버리면?
            cnt += 1
            ans = N - (M - 1) * cnt
    cnt = 0   # 초기화
    print("#{} {}".format(test_case, ans))