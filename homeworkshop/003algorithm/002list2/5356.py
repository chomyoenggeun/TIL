import sys
sys.stdin = open("sample_input.txt", "r")

# 2번

T = int(input())

for tc in range(1, T+1):
    word = [0] * 5

    max_len = 0

    for i in range(5):
        word[i] = list(input())
        if len(word[i]) > max_len:
            max_len = len(word[i])

    print("#{}".format(tc), end = " ")

    for i in range(max_len):
        for j in range(5):
            try:
                print(word[j][i], end = "")
            except:
                pass

    print()





# 1번

T = int(input())

for tc in range(1, T+1):
    word = [0] * 5

    max_len = 0

    for i in range(5):
        word[i] = list(input())
        if len(word[i]) > max_len:
            max_len = len(word[i])

    print("#{}".format(tc), end = " ")

    for i in range(max_len):
        for j in range(5):

            if len(word[j]) > i:
                print(word[j][i], end = "")

    print()

# (1) 문제접근방법은 열우선 순회 방식을 사용

# T = int(input())
# print(T)
# # 제멋대로 받는 경우에는 어떻게 해야되지?
# for test_case in range(1, T+1):
#     arr = [input() for _ in range()]
#     print(arr)

# # 1번 방식
#
# T = int(input())
# for t in range(T):
#     line = 5
#     str_list = [input() for _ in range(line)]
#     print_str = ''
#     max_length = 0
#     #길이가 나와있지 않으므로 최대 길이를 찾는다.
#     for i in range(line):
#         # max함수 안쓰고 해야하는데
#         max_length = max(max_length, len(str_list[i]))
#     #세로로 읽어야 하므로 가로 세로순으로 반복문을 돌려준다.
#     for i in range(max_length):
#         for j in range(line):
#             #현재 읽는 위치가 인덱스를 넘어가지 않는다면 출력문자열에 추가한다.
#             if len(str_list[j]) > i:
#                 print_str += str_list[j][i]
#     print("#{} {}".format(t+1, print_str))



# 2번방식 

# T = int(input())
#
# for tc in range(1, T+1):
#     word = [0] * 5
#     #최대 길이를 담을 값
#     max_len = 0
#
#     for i in range(5):
#         word[i] = list(input())
#         # 입력을 받으면서 최대 길이를 갱신
#         if len(word[i]) > max_len:
#             max_len = len(word[i])
#
#     # 세로로 읽어보자.
#     print("#{}".format(tc), end=" ")
#     for i in range(max_len):
#         for j in range(5):
#             # if len(word[j]) > i:
#             #     print(word[j][i], end="")
#             try:
#                 print(word[j][i], end="")
#             except:
#                 continue
#     print()


#
# # 정성우
#
#
# t=int(input())
# for tc in range(t):
#     words = [input() for _ in range(5)]
#     for i in range(5):
#         if len(words[i])<15:
#             for _ in range(15-len(words[i])): # 단어 길이가 15가 안되면 -로 나머지 공간을 채운다.
#                 words[i]+='-'
#     ans=''
#     for i in range(15):
#         for j in range(5):
#             if words[j][i]!='-':
#                 ans+=words[j][i]
#     print(f'#{tc+1}', ans)
#
#
#




# 실패한 방식



# T = int(input())
# # print(T)
# for test_case in range(1, T+1):
    # arr = list(input().split())
    # print(arr)  # 왜 다 못 읽어내지?
    # 2차원 리스트로 받기
    # 1번 입력방식
    # words = [list(map(str, input().split())) for _ in range(5)]
    # print(words)
    # 열우선 순회 방식
    # for j in range(len(arr[0])):
    #     for i in range(len(arr)):
    #         print(words[i][j], end = ' ')
    # ABCDE abcde 01234 FGHIJ fghij AABCDD afzz 09121 a8EWg6 P5h3kx


    # max_len = 0 # 문자열 최대길이
    # length = [] # 길이 저장 [1, 1, 1, 1, 1]
    # for word in words:
    #     # print(word)
    #     # print(len(word))
    #     length.append(len(word))
    #     # print(length)
    #     if len(word) > max_len:
    #         max_len = len(word)
    # ans = ''
    # for i in range(max_len):
    #     for j in range(5):
    #         if length[j] > i :
    #             ans += words[j][i]
    # print('#{} {}'.format(test_case, ans))

# # 2번 입력방식
# word = [0] * 5
# # words = [input() for _ in range(5)]
# # print(words)
# ans = ''
# max_length = 0 # 최대길이 구분이 필요해서
#
# for k in range(5):
#     word[k] = list(input())
#     # print(word)


