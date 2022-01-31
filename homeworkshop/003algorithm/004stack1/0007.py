def dfs(s, V):
    visited = [0] * (V + 1)
    stack = []
    i = s # 현재 방문한 정점 i
    visited[i] = 1
    # print(node[i])
    while i != 0: # True:
        for w in range(1, V+1): # w는 내가 지금 갈 수 있는지 확인
            if adj[i][w] == 1 and visited[w] == 0:
                print(node[w])
                stack.append(i) # 방문경로 저장
                i = w
                visited[w] =1
                print(node[i])
                break
            else:
                if stack:
                    i = stack.pop()
                else:
                    i = 0
                    # break
    return


#         A  B  C  D  E  F  G
adj = [[0, 0, 0, 0, 0, 0, 0, 0],
       [0, 0, 1, 1, 0, 0, 0, 0], # A
       [0, 1, 0, 0, 1, 1, 0, 0], # B
       [0, 1, 0, 0, 0, 1, 0, 0], # C
       [0, 0, 1, 0, 0, 0, 1, 0], # D
       [0, 0, 1, 1, 0, 0, 1, 0], # E
       [0, 0, 0, 0, 1, 1, 0, 1], # F
       [0, 0, 0, 0, 0, 0, 1, 0]] # G

node = ['', 'A', 'B', 'C', 'D', 'E', 'F', 'G']
print(dfs(1, 7))