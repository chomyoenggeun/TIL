T = int(input())
for test_case in range(1, T+1):
    N = int(input())   # 가로길이
    building = list(map(int, input().split()))

    result = 0

    for i in range(N):
        crush = 0
        # 앞에서 부터 보자
        for j in range(i+1, N):
            if building[i] > building[j]:
                crush += 1

            if crush > result:
                result = crush

    print("#{0} {1}".format(test_case, result))




# # 조명근
# T = int(input())   # test_case 갯수
# for test_case in range(1, T+1):    # T개의 소스코드가 주어진다
# 	N = int(input())        # 가로길이 건물수
#     building = list(map(int, input().split()))      # 건물높이 리스트로 만들기
#
#     crush = 0    # 충격을 0으로 초기화
#     result = 0   # 결과값 초기화
#     for i in range(0, N-1):    # 앞에서부터 보자
#         if building[i] > building[i+1]: # 현재 건물과 다음 건물의 높이 차
#             crush += 1    # 현재 건물이 높으면 충격을 +1
#
#         if crush > result:     # 충격들 중 가장 큰값을 결과 값으로 반환
#             result = crush
#         crush = 0
# 	print("#{0} {1}".format(test_case, result))

