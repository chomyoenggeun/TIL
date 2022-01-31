
# 인접시리즈

# 인접행렬 - 주어진 정점들의 연결관계를 2차원 리스트로 표현한 구조
# A와 B라는 두 개의 정점이 서로 연결되어있는지 확인이 용이
# 간선이 별로 없을때 정점이 매우 낳으면 메모리 손해 극심


V, E = map(int, input().split())

adj_arr = [[0] * V for _ in range(V)]  # 0으로 구성된 2차원 리스트
# print(adj_arr)

for i in range(E):
    start, end = map(int, input().split())
    adj_arr[start][end] = 1 # 표시를 한다, 여기서 끝내면 방향성이 생긴다
    adj_arr[end][start] = 1

for i in adj_arr:  # adj_arr 구현
    print(*i)


# 인접리스트 - 나와 인접한 친구들만 리스트로 만들어 저장
# 장점 연결되어있는 친구들만 넣어놨으니 확인불필요
# 단점 간선이 매우 많으면 이점은 없다

V, E = map(int, input().split())

adj_list = [[] for _ in range(V)] # 빈 2차원 리스트 생성

for i in range(E):
    start, end = map(int, input().split())
    adj_list[start].append(end)
    adj_list[end].append(start)

for i in range(V):
    print("{}번째 연결된 정점은 : {}".format(i, adj_list[i]))


# 간선배열