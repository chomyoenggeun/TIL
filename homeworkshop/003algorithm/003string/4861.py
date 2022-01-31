import sys
sys.stdin = open("sample_input2.txt", "r")


def check():
    for i in range(N):  # 전체 크기가 N
        # 가로 검사
        for j in range(N - M + 1):
            tmp = words[i][j:j + M]

            if tmp == tmp[::-1]:
                return tmp

        # 세로 검사
        for j in range(N - M + 1):
            tmp = []
            for k in range(M):
                tmp.append(words[j + k][i])
            if tmp == tmp[::-1]:
                return tmp

    return []
    # 전체를 도는 for문 끝


T = int(input())

for tc in range(1, T + 1):
    # N : 가로세로 길이
    # M : 회문의 길이
    N, M = map(int, input().split())

    words = [list(input()) for _ in range(N)]

    ans = check()

    print("#{} {}".format(tc, ''.join(ans)))






# 실패한 방법
# T = int(input())
#
# for test_case in range(1, T+1):
#     n, m = map(int, input().split())
#     arr = []
#     for _ in range(n):
#         arr.append(input())
#         # arr.append(list(input()))
#     # print(arr)
#     for i in arr:
#         # print(i)
#         for j in range(n):
#             if i[j] == i[n-1-j]:  # 한번이라도 같으면 안되는구나
#                 result = i # 그래서 계속 같은 값이 나왔네
#                 print(result)




# 정성우

t = int(input())
for tc in range(t):
    n, m = map(int, input().split())
    alphas = [input() for _ in range(n)]
    # 가로로 찾기
    for i in range(n):
        for j in range(n - m + 1): # 인덱스 범위 초과하지않게
            if alphas[i][j:j + m] == alphas[i][j:j + m][::-1]:
                ans = alphas[i][j:j + m]

    # 세로로 찾기
    for i in range(n):
        for j in range(n - m + 1):
            now = ''
            for k in range(m):
                now += alphas[j + k][i]
            if now == now[::-1]:
                ans = now
    print(f'#{tc + 1} {ans}')




#
# T = int(input())
#
# for test_case in range(1, T + 1):
#     n, m = map(int, input().split())
    # # 1번 방법
    # arr = []
    # for _ in range(n):
    #     # arr.append(input())
    #     arr.append(list(input()))

    # 2번 방법
    # arr = [0 for _ in range(n)]
    # # print(n)
    # # print(m)
    # for i in range(n):
    #     arr[i] = list(input())
    # print(arr) # 값받기
    #
    # count = 0
    # print("#{} ".format(test_case, end = ""))
    #
    # # 가로축
    # for i in range(n):
    #     for j in range(0,n-m+1):
    #         for k in range(m//2):
    #             if arr[i][j+k]==arr[i][j+m-1-k]:
    #                 count+=1
    #         if count==m//2:
    #             for l in range(j,j+m):
    #                 print(arr[i][l],end="")
    #         count=0
    # # 세로축
    # count=0
    # for j in range(n):
    #     for i in range(0,n-m+1):
    #             for k in range(m//2):
    #                 if arr[i+k][j]==arr[i+m-1-k][j]:
    #                     count+=1
    #             if count==m//2:
    #                 for l in range(i,i+m):
    #                     print(arr[l][j],end="")
    #         count=0
    # print("")




T = int(input()) # test_case를 받는다
for test_case in range(1, T+1):
    n, m = map(int, input().split())
    arr = [0 for _ in range(n)]
    for i in range(n):
        arr[i] = list(input())   # 리스트를 받아준다.
    # # 1번 방법 통과
    # arr = []
    # for _ in range(n):
    #     # arr.append(input())
    #     arr.append(list(input()))

    # # 2번 방법 - 통과
    # arr = [0 for _ in range(n)]
    # # print(n)
    # # print(m)
    # for i in range(n):
    #     arr[i] = list(input())
    # # print(arr) # 값받기

    count = 0
    print("#{} ".format(test_case), end="")


    for i in range(n):
        for j in range(0, n - m + 1): # 인덱스 범위 안넘게
            for k in range(m // 2):
                if arr[i][j + k] == arr[i][j + m - 1 - k]:
                    count += 1
            if count == m // 2:
                for l in range(j, j + m):
                    print(arr[i][l], end="")
            count = 0
    # 세로축
    count = 0
    for j in range(n):
        for i in range(0, n - m + 1):
            for k in range(m // 2):
                if arr[i + k][j] == arr[i + m - 1 - k][j]:
                    count += 1
            if count == m // 2:
                for l in range(i, i + m):
                    print(arr[l][j], end="")
            count = 0
    print("")






# zip 함수를 이용해서 세로 확인을 할 수 있다.








# 박수아  # 프린트 두 개 X