import sys
sys.stdin = open("input1.txt", "r")
# 문제접근법, 마지막 가격을 알 수 있기때문에 뒤에서 접근

T = int(input())
for tc in range(1,T+1):
    num = int(input())
    # 리스트 순회방식으로 자료받기
    arr = list(map(int,input().split()))
    # print(arr)
    last = arr[-1] # 마지막 가격
    # print(last)
    profit = 0  # 누적 시킬 이익값
    for i in range(len(arr)-1,-1,-1): # 핵심! 뒤부터 보기
        if arr[i] < last : # 마지막 가격보다 작으면
            # print(arr[i])
            profit += last - arr[i]  # 차액을 이익에 더해주고
        else: # 같거나 크다면
            last = arr[i]      # 마지막 가격 갱신
    print("#{} {}".format(tc, profit))


# 최대값 갱신
T = int(input())

for tc in range(1, T+1):
    N = int(input())
    cost = list(map(int, input().split())) # 가격들을 입력 받는다

    ans = 0

    for i in range(N-1): # 마지막 날은 사도 그만 안사도 그만
        max_cost = cost[i]
        for j in range(i+1, N):
            if max_cost < cost[j]:
                max_cost = cost[j]

        if max_cost > cost[i]:
            ans += max_cost - cost[i]  # 차익 구하기

    print("#{} {}".format(tc, ans))



# 팔 수 있는지 없는지 체크

T = int(input())

for tc in range(1, T+1):
    N = int(input())
    cost = list(map(int, input().split()))

    ans = 0

    is_sell = [False] * N  # 0으로 채우기

    for i in range(N-1):
        for j in range(i+1, N):
            if cost[i] < cost[j]:
                is_sell[i] = True
                break

    buy_cost = 0
    buy_cnt = 0

    for i in range(N):
        if is_sell[i]:
            buy_cost += cost[i]
            buy_cnt += 1
        else:
            ans += (cost[i] * buy_cnt) - buy_cost
            buy_cost = 0
            buy_cnt = 0

    print("#{} {}".format(tc, ans))



# 역으로 탐색

T = int(input())

for tc in range(1, T+1):
    N = int(input())
    cost = list(map(int, input().split()))

    ans = 0

    max_cost = cost[-1]

    for i in range(N-2, -1, -1):
        # 내가 가진 값보다 비교 값이 작을때
        if max_cost > cost[i]:
            ans += max_cost - cost[i]  # 차익 더해주기
        else:
            max_cost = cost[i] # 최대값 갱신

    print("#{} {}".format(tc, ans))