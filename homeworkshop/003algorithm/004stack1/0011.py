# 스택2

# 시작점을 스택에 넣고 시작한다.

# 스택이 공백이 될때까지 반복을 수행한다.

# 스택에서 하나 꺼낸다.
# 해당 정점이 방문하지 않은 정점이라면 방문처리하고
# 연결된 친구들을 모조리 스택에 push한다.

def DFS(st):
    stack = []
    stack.append(st)

    while stack:
        curr = stack.pop()  # 스택에서 하나 꺼내기

        # if vistied[curr] : continue
        if not visited[curr]:
            visited[curr] = True

            print(chr(curr + 65), end=' ')

            for i in range(V):
                if adj_arr[curr][i] and not visited[i]:
                    stack.append(i)


V, E = map(int, input().split())

adj_arr = [[0] * V for _ in range(V)]
visited = [False] * V

for i in range(E):
    st, ed = map(int, input().split())
    adj_arr[st][ed] = 1  # 여기서 끝내면 방향성있는 표시
    adj_arr[ed][st] = 1

DFS(0)


#
# def DFS(st):
#     stack = []
#     stack.append(st)
#
#     while stack:
#         curr = stack.pop() # 스택에서 하나 꺼내기
#         # if visited[curr]:
#         #     continue
#         if not visitied[curr]:
#             visitedp[curr] = True
#
#             print(chr(curr+65), end = ' ')
#
#             for i in range(V):
#                 if adj_arr[curr][i] and not visited[i]:
#
#
#
# V, E = map(int, input().split())
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