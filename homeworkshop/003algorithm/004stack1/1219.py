import sys
sys.stdin = open('input3.txt', 'r')

def DFS(v):
    global ans
    if v == 99:
        ans = 1
        return

    visited[v] = 1

    for w in range(100):
        if not visited[w] and adj_arr[v][w]:
            DFS(w)


for _ in range(10):
    tc, N = map(int, input().split()) # tc는 테스트케이스, N은 길의 갯수
    road = list(map(int, input().split()))

    adj_arr = [[0] * 100 for _ in range(100)]

    for i in range(N):
        adj_arr[road[2*i]][road[2*i+1]] = 1

    visited = [0] * 100
    ans = 0

    DFS(0)
    print('#{}  {}'.format(tc, ans))



# # 길찾기
#
# for _ in range(1):
#     tc, N = map(int, input().split()) # tc는 테스트케이스, N은 길의 갯수
#     road = list(map(int, input().split()))
#
#     # 1. 홀짝
#     # 2. 2step
#     # 3. 2*?
#
#     for i in  range(N):
#         st = road[2*i]
#         ed = road[2*i+1]
#         print(st, ed)
#
#     ##############################################
#     # 저장방법
#     # 1. ch1, ch2
#     ch1 = [0] * 100
#     ch2 = [0] * 100
#
#     for i in range(N):
#         if ch1[road[2*i]] == 0:
#             ch1[road[2*i]] == road[2*i+1]
#         else:
#             ch2[road[2*i]] == road[2*i+1]
#
#     # 2. 인접행렬 방식
#     adj_arr = [[0] * 100 for _ in range(100)]
#     for i in range(N):
#         adj_arr[road[2*i]][road[2*i+1]] = 1
#
#     # 3. 인접리스트 방식
#     adj_list = [[] for _ in range(100)]
#     for i in range(N):
#         adj_list[road[2*i]].append(road[2*i+1])
#
#
#
# for _ in range(10):
#     tc, N = map(int, input().split())  # tc는 테스트케이스, N은 길의 갯수
#     road = list(map(int, input().split()))
#
#     adj_list = [[] for _ in range(100)]
#     for i in range(N):
#         adj_list[road[2*i]].append(road[2*i+1])
#
#     visited = [0] * 100
#     ans = 0
#
#     stack = [0]
#
#     while stack: # 값이 존재해?
#         curr = stack.pop()
#         if curr == 99:
#             ans = 1
#             break
#         # 방문하지 않았으면
#
#         # 방문을 했으면, 건너가
#         if visited[curr]:
#             continue
#         visited[curr] = 1
#
#         for w in adj_list[curr]:
#             if not visited[w]:
#                 stack.append(w)
#     print('#{} {}'.format(tc, ans))
#
#
#


# 내답
#
# def dfs(v): # v: 시작점
#     # visited 체크: 하고픈 일 해라(출력)
#     visited[v] = True # 1로 체크
#     # print(v, end=" ")
#     # 시작정점(v)의 인접한 모든 점정 (w) for 돌리기
#         # 인접정점(w)가 방문하지 않았으면
#     for w in range(1, V+1):
#         if adj[v][w] == 1 and visited[w] == 0:
#             # 다시 dfs(w) 재귀 호출
#             dfs(w)
#
# for _ in range(10):
#
#     V = 100
#     tc, E = map(int, input().split()) # V: 정점재수, E:간선갯수
#     # print(tc, E)
#     tmp = list(map(int, input().split())) # 2차원 리스트 데이터 받기
#     # print(tmp)
#     adj = [[0]* (V+1) for _ in range(V+1)] # 인접행렬 초기화
#     visited = [0] * (V+1)  # 방문 행렬
#
#     # 입력
#     for i in range(E):
#         s, e = tmp[2*i], tmp[2*i+1]
#         adj[s][e] = 1
#
#     # for i in range(V+1):
#     #     print("{} {}".format(i, adj[i]))
#
#     print("#{}".format(tc),end=' ')
#     dfs(0)  # A도시
#
#     if visited[99] == True:
#         print(1)
#     else:
#         print(0)
