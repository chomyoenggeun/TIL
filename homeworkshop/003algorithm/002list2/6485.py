import sys
sys.stdin = open("s_input.txt", "r")
#
# # 모든 노선을 체크하는 방법
# def bus_count(bus_stop):
#     cnt = 0
#
#     for i in range(N):
#         if bus_route[i][0] <= bus_stop <= bus_route[i][1]: # 나누어서 쓰는 경우도 알자
#             cnt += 1
#
#     return cnt
#
# T = int(input())
# # print(T)
# for tc in range(1, T+1):
#     N = int(input()) # 노선의 수
#     # print(N)
#     bus_route = [] # 버스 노선들을 저장할 리스트
#
#     for i in range(N):
#         A, B = map(int, input().split())
#         bus_route.append((A, B)) # 튜플형태로 받는다 # 튜플과 리스트형식의 차이점을 알고쓰자
#
#     # 내가 확인하고 싶은 정류장의 갯수
#     P = int(input())
#     ans = [] # 버스 수를 저장해 놓을 리스트
#
#     for i in range(P):
#         C = int(input())
#         ans.append(bus_count(C))
#
#     print('#{}'.format(tc), end = " ")
#     print(' '.join(map(str, ans)))



# 정류장 미리 계산

T = int(input())
# print(T)
for tc in range(1, T+1):
    N = int(input()) # 노선의 수

    start = [0] * 5001     # 출발 정류장 표시
    end = [0] * 5001       # 도착 정류장 표시
    bus_stop = [0] * 5001

    for i in range(N):
        A, B = map(int, input().split())
        start[A] += 1
        end[B] += 1

    # 버스 계산 끝
    for i in range(len(bus_stop)-1):
        bus_stop[i+1] = bus_stop[i] - end[i] + start[i+1]

    P = int(input())
    print('#{}'.format(tc), end = " ")

    for i in range(P):
        C = int(input()) # 우리가 확인하고 싶은 정류장 번호
        print(bus_stop[C], end = " ")
    print()


# 3. 미리계산2

T = int(input())
# print(T)
for tc in range(1, T+1):
    N = int(input()) # 노선의 수

    bus_stop = [0] * 5001

    for i in range(N):
        A, B = map(int, input().split())

        for j in range(A, B+1):
            bus_stop[j] += 1
    P = int(input())

    print('#{}'.format(tc), end = " ")

    for i in range(P):
        C = int(input()) # 우리가 확인하고 싶은 정류장 번호
        print(bus_stop[C], end = " ")
    print()


#
#
# 문찬솔
#
# T = int(input())
# for tc in range(1, T + 1):
#     # 1번~5000번의 버스정류장
#     bus_stop = [0 for i in range(5000)]
#     # N :버스 노선의 개수
#     N = int(input())
#     for _ in range(N):
#         a, b = map(int, input().split())
#         # 버스가 지나는 정류장 카운트 증가
#         for i in range(a - 1, b):
#             bus_stop[i] += 1
#     # P개의 버스 정류장에 대해
#     P = int(input())
#     answer = ''
#     for _ in range(P):
#         # answer문자열에 입력된 정류장의 버스가 지나간 횟수를 문자열+공백으로 추가
#         answer += str(bus_stop[int(input()) - 1]) + ' '
#
#     print('#{} {}'.format(tc, answer[:-1]))
#
#
#
# # 정성우
#
# t = int(input())
# for tc in range(t):
#     n = int(input())
#     # 노선 정보 추가
#     buslane = []
#     # 요 입력이 안됨
#     for _ in range(n):
#         a, b = map(int, input().split())
#         buslane.append((a, b))
#         # print(buslane)
#     p = int(input())
#
#     # 확인할 정류장 p개 입력
#     checkstop = [int(input()) for _ in range(p)]
#
#     ans = []
#     # 정류장마다 노선이 지나가는지 체크해서 카운트
#     for stop in checkstop:
#         cnt = 0  # 버스 정류장 입력에 중복이 있을 수도 있어서 초기화가 필요함!!!!!!!!!!!!!!!!!!!!!!
#         for a, b in buslane:
#             if a <= stop <= b:
#                 cnt += 1
#         ans.append(cnt)
#
#     print(f'#{tc + 1}', ' '.join(map(str, ans)))