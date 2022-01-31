import sys
sys.stdin = open('sample_input2.txt', 'r')

# 문제접근 스택2방식

T = int(input())
# print(T)
def DFS(one, last): # one 시작점 last 끝점
    # 스택을 빈리스트로 초기화
    stack = []
    # visited으로 방문검사
    # 인덱스 값이라서 +1
    visited = [False] * (V+1)
    # 스택에 시작점을 삽입한다.
    stack.append(one)

    # 스택이 빌때까지 반복문을 돌려준다.
    while stack:
        # 지금 현재 스택을 꺼내서 현재 값에 할당
        instant = stack.pop()
        # 현재 방문표기
        visited[instant] = True
        # after 다음 간선, V+1범위까지 살펴본다
        for after in range(1, V+1):
            # 만약 방문하지않았고, 연결되어있으면 값이 1이라면
            if not visited[after] and adj_arr[instant][after]:
                # 갈 수 있으므로 스택에 push
                stack.append(after)
    # 만약 끝점에 들렀었다면
    if visited[last]:
        # 1값 반환
        return 1
    else:
        # 아니라면 0
        return 0

for tc in range(1, T+1):
    # 정점과 간선 데이터를 받는다.
    V, E = map(int, input().split())
    # 여기서 실수 # v+1개 V+1개 제발 바보야
    adj_arr = [[0] * (V+1) for _ in range(V+1)] # 0으로 구성된 2차원리스트 만들기
    # print(adj_arr)
    for i in range(E):
        # 시작점과 끝점을 받는다.
        start, end = map(int, input().split())
        # print(start, end)
        adj_arr[start][end] = 1

    # for i in adj_arr: # 인접행렬 구현
    #     print(*i)
    # 검사를 위한 시작점 끝점을 받는다.
    sta, en = map(int, input().split())

    print('#{} {}'.format(tc, DFS(sta, en)))




# 깔끔버젼

Test_case=int(input())

def DFS(start, end): #DFS함수를 만드는데 시작과 끝을 인자로 받는다.
    stack=[]         #빈 스택 생성
    visited=[False]*(V+1)  #경로에 있는지 없는지 확인
    stack.append(start)    #start인수를 스택에 추가

    while stack:           #stack이 비어있는 동안
        now=stack.pop()    #stack을 pop으로 꺼내 현재값 지정
        visited[now]=True  #현재값이 방문했다면
        for i in range(1, V+1):  #1부터 V까지의 숫자까지(V는 가장 큰 숫자)
            if not visited[i] and node[now][i]: #만약 i번째에 방문하지 않고 연결되어있다면
                stack.append(i) #경로로 될수 있으므로 stack에 추가해준다.
    if visited[end]: #만약 끝점을 갔었다면
        return 1    #1을 반환하고
    else:
        return 0    #아니면 0을 반환한다.


for t in range(1,Test_case+1):
    V, E=map(int,input().split()) #V는 가장큰 숫자, E는 경로의 수(간선의 수)
    node=[[0 for i in range(V+1)] for j in range(V+1)] #리스트 내포기능으로 노드를 행렬형태로 0을 채워 만들어준다.
    for _ in range(E):
        start, end=map(int, input().split())
        node[start][end]=1

    start, end=map(int, input().split())
    print("#{} {}".format(t, DFS(start,end)))

t = int(input())



# 정성우

def dfs(start):
    v[start] = 1

    for i in graph[start]:
        if not v[i]:
            dfs(i)


for tc in range(t):
    V, E = map(int, input().split())
    graph = [[] for _ in range(V + 1)]
    v = [0] * (V + 1)
    for _ in range(E):
        a, b = map(int, input().split())
        graph[a].append(b)
    s, g = map(int, input().split())
    dfs(s)
    print(f'#{tc + 1} {v[g]}')



# 재귀버전

T = int(input())

def dfs(v): # v: 시작정점
    # visited 체크: 하고픈 일 해라(출력)

    visited[v] = True
    # print(v, end=" ")

    # 시작정점(v)의 인접한 모든 점정 (w) for 돌리기
    for w in range(1, V+1):
        # 인접정점(w)가 방문하지 않았으면
        if adj[v][w] == 1 and visited[w] == False:
            # 다시 dfs(w) 재귀 호출
            dfs(w)

for tc in range(1,T+1):
    V, E = map(int, input().split())  # V: 정점재수, E:간선갯수


    # 0 행렬 그래프 생성: 숫자는 1부터 시작하기 때문에 1개 더 추가
    adj = [[0] * (V+1) for _ in range(V+1)]  # 인접행렬 초기화
    # 지나간 길인지 확인 행렬: 숫자는 1부터 시작하기 때문에 1개 더 추가
    visited = [0] * (V+1)


    # 입력
    for _ in range(E):
        tmp = list(map(int, input().split()))
        s, e = tmp[0], tmp[1]
        adj[s][e] = 1

    # 확인 할 출발 노드 S G
    S, G = map(int, input().split())
    # print(S, G)

    # 행렬 그래프 확인
    # for i in range(V+1):
        # print("#{} {}".format(i, adj[i]))

    # 함수 실행
    dfs(S)

    if visited[G] == 1:
        print("#{} 1".format(tc))
    else:
        print("#{} 0".format(tc))

    # print('--------------')