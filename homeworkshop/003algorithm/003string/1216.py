import sys
sys.stdin = open("inputs.txt", "r")

def check(M):
    for i in range(N):
        for j in range(N - M + 1):
            # 가로
            tmp = words[i][j:j + M]
            # 세로
            tmp2 = zwords[i][j:j + M]

            if tmp == tmp[::-1] or tmp2 == tmp2[::-1]:
                return M
    return 0

for tc in range(10):
    tc_num = int(input())

    N = 100

    words = [list(input()) for _ in range(N)]
    zwords = list(zip(*words))

    for k in range(100, 0, -1):
        ans = check(k)
        if ans != 0:
            break

    print("#{} {}".format(tc_num, ans))


#  틀린답
def find(m):
    for i in range(N):
        for j in range(N - m + 1):
            for k in range(m // 2):
                if p[i][j + k] != p[i][j + m - 1 - k]:
                    break
                elif k == m // 2 - 1:
                    return m
            for k in range(m // 2):
                if p[j + k][i] != p[j + m - 1 - k][i]:
                    break
                elif k == m // 2 - 1:
                    return m
    return 0


for tc in range(10):
    tn = int(input())
    N = 100
    p = [input() for i in range(N)]
    for len in range(100, 0, -1):
        ans = find(len)
        if ans != 0:
            break
    print('#{} {}'.format(tn, ans))
#
# # 회문 2
# # 접근방법 : 가장 긴 회문부터 접근한다.
#
# for test_case in range(1, 11):
# # for test_case in range(1, T+1)
# #     print(test_case)
#     N = 100
#     # arr = [list(map(str, input().split())) for _ in range(N)]
#     # print(arr)
#     words = [list(input()) for _ in range(N)]
#     print(words)
#
#
# #
# #
# def find_palindrome(N, arr):
#     ans = ''
#     for n in range(100):  # 돌아가는 갯수 늘리기
#         for s in range(n+1):  # 탐색 위치 바꾸기
#             for r in range(N): # 한줄씩 바꾸기
#                 flag = True
#                 M = N - n
#                 #가로
#                 for idx1 in range(M // 2): # 앞뒤 비교하는것
#                      start = s + idx1
#                     end = s + M - 1 - idx1
#                     if arr[r][start] != arr[r][end]:
#                         flag = False
#                         break
#                 if flag:
#                     return len(arr[r][s:s + M])
#                 #세로
#                 flag = True
#                 for idx2 in range(M // 2):  # 앞뒤 비교하는것
#                     start = s + idx2
#                     end = s + M - 1 - idx2
#                     if arr[start][r] != arr[end][r]:
#                         flag = False
#                         break
#                 if flag:
#                     for i in range(M):
#                         ans += arr[s+i][r]
#                     return len(ans)
#
#
# for _ in range(10):
#     tc = int(input())
#     arr = []
#     N = 100
#     for i in range(N):
#         arr.append(list(input()))
#     print('#{} {}'.format(tc, find_palindrome(N, arr)))
