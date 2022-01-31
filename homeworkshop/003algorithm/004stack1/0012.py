# DFS 재귀

# 인접행렬 방법

def DFS(curr):
    visited[curr] = True
    print(chr(curr+65), end=' ')

    for i in range(V):
        if adj_arr[curr][i] and not visited[i]:
            DFS(i)


V, E = map(int, input().split())

adj_arr = [[0] * V for _ in range(V)]
visited = [False] * V

for i in range(E):
    st, ed = map(int, input().split())
    adj_arr[st][ed] = 1  # 여기서 끝내면 방향성있는 표시
    adj_arr[ed][st] = 1

DFS(0)

# 인접리스트
def DFS(curr):
    #방문쳌
    visited[curr] = True
    print(chr(curr+65), end=' ')

    #방문하지 않고 인접한 정점으로 이동
    for i in adj_list[curr]:
        if not visited[i]:
            DFS(i)


V, E = map(int, input().split())

adj_list = [[] for _ in range(V)] #인접리스트
visited = [False] * V #방문쳌을 위한

for i in range(E):
    st, ed = map(int, input().split())
    adj_list[st].append(ed)  # 여기서 끝내면 방향성있는 표시
    adj_list[ed].append(st)

DFS(0)

# 인접리스트

# def DFS(curr):
#     visited[curr] = True
#     print(chr(curr+65), end = ' ')
#
#     for i in range(V):
#         if adj_arr[curr][i] and not visited[]
#
#
#
# adj_arr = [[0] for _ in range(V)] # 빈 2차원 리스트 생성
# visited = [False] * V
#
# for i in range(E):
#     start, end = map(int, input().split())
#     adj_arr[start][end] = 1
#     adj_arr[end][start] = 1
#
# DFS(0)