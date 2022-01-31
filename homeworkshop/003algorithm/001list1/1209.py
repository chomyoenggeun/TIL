# 조명근

T = 10
N = 100

# 가정은 행의 합은 행우선 순회, 열의 합은 열우선 순회, 대각선은 아래에서
for test_case in range(1, T+1):   # test_case 10개 받는다.

    number = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]

    max_value = 0 # 최대값 초기화  , 양수값일때만 허용

    # 행의 합 => 행우선 순회 100*100
    for i in range(N):
        sum_value = 0    # 행의 합 초기화, 초기화 위치가 너무 중요하다
        for j in range(N):
            sum_value += arr[i][j]
        if sum_value > max_value:
            max_value = sum_value  # 최대값 갱신

    # 열의 합 => 열우선 순회
    for i in range(N):
        sum_value = 0   # 열의 합 초기화
        for j in range(N):
            sum_value += arr[j][i]
        if sum_value > max_value:
            max_value = sum_value   # 행의 최대값은 남아있고 열로 갱신

    # 대각 합1 => 왼상우하
    sum_value = 0     # 이중 for문을 돌지않기 때문에 밖에 배치
    for i in range(N):
        sum_value += arr[i][i]
        if sum_value > max_value:
            max_value = sum_value  # 최대값 갱신

    # 대각 합2 => 왼하우상 /
    sum_value = 0
    for i in range(N):
        sum_value += arr[i][N-1-i]     # 정신병 걸리는 줄 알았다...
        if sum_value > max_value:
            max_value = sum_value  # 최대값 갱신

    print("#{} {}".format(number, max_value))





# 양지훈

def our_max(a, b):
    if a > b: return a
    return b
 
 
def max_sum():
    for tc in range(1, 11):
        T = int(input())
        arr = [list(map(int, input().split())) for a in range(100)]
        ans = arr[0][0]
        row, col, dia, r_dia = arr[0][0], arr[0][0], arr[0][0], arr[0][0]
        for i in range(100):
            for j in range(100):
                row += arr[i][j]
                col += arr[j][i]
                if i == j:
                    dia += arr[i][j]
                if i + j == 99:
                    r_dia += arr[i][j]
            if our_max(row, col) > ans:
                ans = our_max(row, col)
            row, col = 0, 0
        if our_max(dia, r_dia) > ans:
            ans = our_max(dia, r_dia)
 
        print("#{} {}".format(T, ans))
 
 
max_sum()



# 강동옥

def myMax(nums):                  # 입력한 숫자 중 최댓값을 구하는 함수
    max_num = nums[0]

    for num in nums:
        if max_num < num:
            max_num = num

    return max_num

def arrSum(direction, r=0, c=0):  # 지정한 방향으로 진행하며 합을 구하는 함수
    result = 0

    if direction[1] < 0:          # 좌하향일 경우 c는 99부터 시작
        c = 99

    for _ in range(100):          # 지정한 방향으로 이동하며 값 더함
        result += arr[r][c]
        r += direction[0]
        c += direction[1]

    return result

####

for _ in range(10):
    tc = int(input())
    arr = [list(map(int, input().split())) for _ in range(100)]

    drc = [     # 갈수있는 방향
        (1,0),  # 세로
        (0,1),  # 가로
        (1,1),  # 우하향
        (1,-1)  # 좌하향
    ]

    sum_list = []           # 합을 저장할 리스트생성

    for n in range(100):    # 행과 열을 순회하며 모든 가로세로 합 계산
        sum_list.append(arrSum(drc[0], c=n))    # 세로방향 합, 열 순회
        sum_list.append(arrSum(drc[1], r=n))    # 가로방향 합, 행 순회

    for rc in drc[2:]:      # 대각선 합 계산
        sum_list.append(arrSum(rc))

    print('#{} {}'.format(tc, myMax(sum_list))) # 합 중 최댓값을 형식에 맞게 출력
