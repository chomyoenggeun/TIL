# 사다리타기1
import sys

sys.stdin = open("input.txt", "r")

def search(start): # 도착지에서 위로 올라가는 함수
    i = 99 # 행
    j = start # 열
    # 행이 0이될때까지 올라간다.
    while i > 0:
        i -= 1 # 위로 한 칸 이동
        # 왼쪽검사 오른쪽 검사 후 위로 검사
        if j>0 and ladder[i][j-1] == 1: # 왼쪽이동 조건, 왼쪽 칸이 1이면
            while j>0 and ladder[i][j-1] == 1: # 사다리를 벗어나거나 0일때 까지
                j -= 1       # 왼쪽 이동
        elif j < 99 and ladder[i][j+1] == 1: # 오른쪽 이동 조건, 오른쪽 칸이 1이면
            while j < 99 and ladder[i][j+1] == 1: # 0을 만날때 까지 쭉가
                j += 1    # 오른쪽 이동
    return j # 0번 행에 열(출발지) 리턴


T = 10
for test_case in range(1, T+1):
    n = int(input())
    ladder = [list(map(int, input().split())) for _ in range(100)]
    # print(ladder)
    # 도착지 검색
    goal = 0
    for i in range(100):
        if ladder[99][i] == 2:
            goal = i
    ans = search(goal)
    print("#{} {}".format(test_case, ans))