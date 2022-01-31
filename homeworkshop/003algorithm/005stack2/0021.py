# counting 1단계

arr = [3,4,5,7,7,7,5]

cnt = 0 #target 의 개수를 세도록
for i in range(0,7):
    if arr[i] == 7 :
        cnt += 1

print(cnt)

arr = [3,4,5,7,7,7,5]

cnt = 0 # 홀수의 개수 카운트
for i in range(7):
    if arr[i] % 2 == 1 :
        cnt += 1

print(cnt)

# 카운팅 2단계

arr = [
    [3,2,5,9],
    [1,2,3,4],
    [5,5,7,7],
]

cnt = 0
for r in range(3): # r 을 먼저 선택
    for c in range(4):
       #3 <= arr[r][c] <= 4
        if 3 <= arr[r][c] and arr[r][c] <= 4:
            cnt += 1

print(cnt)

# flag 1단계

arr = [3,2,7,5,3,7,1]

flag = 0

for i in range(7):
    if arr[i] == 7 :
        flag = 1
        break

if flag == 0 :
    print("안존재")
else :
    print("존재")


# flag 2단계

arr = [
    [3,2,7,5],
    [1,7,1,7],
    [1,2,3,4]
]

flag = 0

for r in [0,1,2] :
    for c in [0,1,2,3] :
        if arr[r][c] == 7:
            flag = 1
            break
    if flag == 1 :
        break

if flag == 0 :
    print("안존재")
else :
    print("존재")


# 공백으로 구분된 2차원 리스트 입력하기

arr = [
    list(map(int,input().split())) for _ in range(3)
]
de = -1

str_ = "ATCKB"

for s in range(5):
    # s ~ 4
    for x in range(s,4+1):
        print(str_[x],end='')
    print()

str_ = "ATCKB"

for e in range(4,-1,-1):
    for x in range(0,e+1):
        print(str_[x],end ='')
    print()


# 변수 추가로 이용하기

lst = [0,0,0,0,0,0]
num = int(input())
t = num
for i in range(6):
    lst[i] = t
    t += 2
de = - 1

# sum

import sys
sys.stdin = open("text.txt", "r")

T = 10
for tc in range(1, T+1):
    tmp = input()
    arr = [
        list(map(int,input().split())) for _ in range(100)
    ]
    de = -1
    max_sum = int(-21e8) # -21억
    # 가로라인 합구하기
    for r in range(100):
        # r 이 하나 고정이됨
        sum = 0
        for c in range(100):
            sum += arr[r][c]
        #sum vs max_sum
        if max_sum < sum :
            max_sum = sum
    # 세로라인 합구하기
    for c in range(100):
        # c 이 하나 고정이 됨
        sum = 0
        for r in range(100):
            sum += arr[r][c]
        # sum vs max_sum
        if max_sum < sum :
            max_sum = sum
    de = - 1
    # 대각선 \
    # 대각선 /

# is_exist 함수

def is_exist(target):
    for i in range(6):
        if target == lst[i]:
            return 1 # 바로 리턴/ 함수가 종료 복귀

    return 0 # for 문 다 돌았는데도 없다

lst = [3,2,1,7,5,9]
ret = is_exist(7)
if ret == 1:
    print("존재")
else :
    print("안존재")



##

arr = [
    [3,2,1,7],
    [1,2,3,4],
    [7,5,2,1],
]

def is_exist(target, row) :
    # arr[row][0~3]
    for c in range(4) :
        if arr[row][c] == target :
            return 1

    return 0

cnt = 0
for r in range(3) :
    ret = is_exist(7,r)
    if ret == 1:
        cnt += 1

print(cnt,"row 개")