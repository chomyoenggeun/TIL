T = int(input()) # test_case 갯수


for test_case in range(1, T+1):
    K, N, M = map(int, input().split())   # K는 정류장 수, N은 종점, M은 충전기 수
    charge = list(map(int, input().split()))  # 충전기 위치

    bus_stop = [0] * (N+1)

    # # 충전소 표시1
    # for i in charge:
    #     bus_stop[i] = 1
    
    # 충전소 표시2
    for i in range(M):
        bus_stop[charge[i]] = 1
    
    # 버스의 위치
    bus_idx = 0
    ans = 0

    # 무한루프 주의
    while True:
        # 일단이동  # 버스가 이동할 수 있는 만큼은 무조건 간다
        bus_idx += K
        if bus_idx >= N:
            break     # 종점에 도착하거나 종점을 나는 경우 종료


        for i in range(bus_idx, bus_idx-K, -1):
            if bus_stop[i]:
                ans += 1
                bus_idx = i
                break

        else:
            ans = 0
            break

    print("#{} {}".format(test_case, ans))
