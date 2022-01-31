import sys
sys.stdin = open('sample_input5.txt', 'r')

# 접근방법1 : 세로 고정, 가로만 공략하자 폐기처분 # 이거 안됨 왜 why 눕는경우 때문에 안됨


# 접근방법2 : 점화식
# 접근방법3 : 점화식인데 메모이제이션쓰기
# 가로길이 카운트하는 함수
def nums(N):
    if memo[N] == -1:
        memo[N] = nums(N-1) + (2 * nums(N-2))
    return memo[N]


T = int(input())
for tc in range(1, T+1):
    # 가로길이 area
    area = int(input())
    # 이건 접근방법2해보고 생각
    memo = [-1] * ((area//10)+1)
    memo[0] = 0
    memo[1] = 1
    memo[2] = 3
    # print(area)
    # 단위가 너무 커서 가로길이 10으로 나누어준다 (인덱스처럼 생각)
    N = area // 10
    # nums(N)
    # print(memo)
    print('#{} {}'.format(tc, nums(N)))








# 접근방법2 : 점화식
# 가로길이 카운트하는 함수
def nums(cnt):
    # 없는 경우
    if not cnt:
        return 0
    # 길이 1인 경우, 10일때 1가지
    if cnt == 1:
        return 1
    # 길이 2인 경우, 20일때  3가지
    elif cnt == 2:
        return 3
    else:
        return nums(area-1)+ (2 * nums(area-2))

T = int(input())
for tc in range(1, T+1):
    # 가로길이 area
    area = int(input())
    # print(area)
    # 단위가 너무 커서 가로길이 10으로 나누어준다. (인덱스처럼
    cnt = nums(area // 10 )
    print('#{} {}'.format(tc, cnt))



# 점화식 1
def paper(n):
    if n == 1:
        return 1
    elif n == 2:
        return 3
    return paper(n - 1) + (2 * paper(n - 2))

T = int(input())
for t in range(1, T + 1):
    n = int(input())
    cnt = paper(n // 10)
    print("#{} {}".format(t, cnt))
#
#

# 점화식2
def fibo(n):
    # 함수 점화식 생성
    if n == 0:
        return 0
    elif n == 1:
        return 1
    return fibo(n - 1) + (2 * fibo(n - 2))


for t in range(int(input())):
    print("#{} {}".format(t + 1, fibo((int(input()) // 10) + 1)))