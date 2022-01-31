# 이진탐색

T = int(input())

for test_case in range(1, T+1):
    N = int(input())
    arr = list(map(int, input().split()))

# 가정 버블 정렬을 이용해서 짝수 인덱스와 홀수 인덱스를 나눠보자
    for i in range(len(arr)):
        if i % 2 == 0:
            for j in i:
                arr[j]



# 정성우

t = int(input())


def binarysearch(p, target):
    l = 1
    r = p
    cnt = 0
    while l <= r:
        mid = int((l + r) / 2)
        cnt += 1
        if mid == target:
            return cnt
        elif mid > target:
            r = mid
        else:
            l = mid

    return 1000


for tc in range(t):
    p, a, b = map(int, input().split())
    acnt = binarysearch(p, a)
    bcnt = binarysearch(p, b)

    if acnt > bcnt:
        win = 'B'
    elif acnt < bcnt:
        win = 'A'
    else:
        win = 0
    print('#{} {}'.format(tc + 1, win))
