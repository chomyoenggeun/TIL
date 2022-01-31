import sys
sys.stdin = open("sample_input.txt", "r")

T = int(input())

for tc in range(1, T+1):
    iron_bar = input()

    cnt = 0 # 막대수
    ans = 0

    for i in range(len(iron_bar)):
        # 열린 괄호면 넣어
        if iron_bar[i] == '(':
            cnt += 1
        elif iron_bar[i -1] == '(':
            cnt -= 1
            ans += cnt
        else:
            cnt -= 1
            ans += 1

    print("#{} {}".format(tc, ans))


# # 막대기 세기
#
# # 쇠막대기 자르기
#
# T = int(input())
#
# for tc in range(1, T+1):
#     iron_bar = input()
#
#     cnt = 0 # 막대수
#     ans = 0
#
#     for i in range(len(iron_bar)):
#         # 열린 괄호면 넣어
#         if iron_bar[i] == '(':
#             cnt += 1
#         else:
#             # 아니라면 빼
#             cnt -= 1
#             if iron_bar[i-1] == '(':
#                 # 얘는 레이저니까
#                 ans += cnt
#             else:
#                 ans += 1
#
#     print("#{} {}".format(tc, ans))






# # 쇠막대기 자르기
#
# T = int(input())
#
# for tc in range(1, T+1):
#     iron_bar = input()
#
#     stack = []
#     ans = 0
#
#     for i in range(len(iron_bar)):
#         # 열린 괄호면 넣어
#         if iron_bar[i] == '(':
#             stack.append('(')
#         else:
#             # 아니라면 빼
#             stack.pop()
#             if iron_bar[i-1] == '(':
#                 # 얘는 레이저니까
#                 ans += len(stack)
#             else:
#                 ans += 1
#
#     print("#{} {}".format(tc, ans))









#
#
# # 김태현
#
# T = int(input())
# for tc in range(1, T+1):
#     # 괄호는 input으로 받는다.
#     iron_bar = input()
#     # print(iron_bar)
#     cnt = 0 # 막대 수 초기화
#     ans = 0 # 결과값 초기화
#
#     # 괄호의 수만큼 for문을 돈다.
#     for i in range(len(iron_bar)):
#         # 열린 괄호에서 막대 추가
#         if iron_bar[i] == '(':
#             cnt += 1
#         else:
#             # 닫힌 괄호라면 막대감소
#             # 레이저라면 당연히 잘못 세었으니까 빼는게 맞다.
#             # 아니라면 어차피 철봉 끝이니 빼는게 맞다.
#             cnt -= 1
#
#             # 레이저
#             if iron_bar[i-1] == '(':
#                # 레이저로 인해서 잘린 막대들이 생겼으므로
#                ans += cnt  # 막대누적
#             else:
#                 # 막대 끝이라는 뜻
#                 ans += 1
#
#     print("#{} {}".format(tc, ans))
#
#
#
#


#
#
#
# # stack
#
# # stack으로 풀기
# T = int(input())
#
# for tc in range(1, T + 1):
#     iron_bar = input()
#
#     # 실제로 철봉이 담길 리스트
#     s = []
#     ans = 0
#
#     for i in range(len(iron_bar)):
#         # 열릴 괄호라면 s 리스트에 넣어놓기
#         if iron_bar[i] == '(':
#             s.append('(')
#         # 닫힌 괄호라면
#         else:
#             # 무조건 꺼내기
#             s.pop()
#
#             if iron_bar[i - 1] == '(':
#                 ans += len(s)
#             else:
#                 ans += 1
#     print("#{} {}".format(tc, ans))
#
#

#
# # 김태현
#
# T = int(input())
#
# for tc in range(1, T + 1):
#     pipes = input()
#
#     # 스택이용
#     stack = []
#     top = -1
#
#     cnt = 0  # 잘린 파이프를 셀 변수
#
#     i = 0
#     while i < len(pipes):
#         # 레이저를 만났을 때
#         if pipes[i] == '(' and pipes[i + 1] == ')':
#             if top == -1:  # 지나가는 파이프가 없는 경우
#                 pass
#             else:  # 레이저 보다 앞에 파이프가 있다는 뜻이므로 잘린 파이프 세어줍니다.
#                 cnt += top + 1
#             i += 2  # 레이져 부분만큼 인덱스 이동
#
#         # 파이프 시작 부분은 스택에 넣어줍니다.
#         elif pipes[i] == '(':
#             stack.append('(')
#             top += 1
#             i += 1
#
#         # 파이프 끝 부분은 잘려진 끝 쪽 조각 하나를 카운트하고 시작 부분을 스택에서 뺍니다.
#         else:
#             stack.pop()
#             top -= 1
#             cnt += 1
#             i += 1
#
#     print('#{} {}'.format(tc, cnt))
