

# Stakc1



## 1. stack 구현하기

```python
# stack 구현하기

def push(item):
    s.append(item) # append를 통해 마지막 데이터를 삽입

def pop():
    if len(s) == 0:
        print("Stack is Empty!!") # underflow
        return
    else:
        return s.pop(-1)  # pop을 통해 마지막 데이터 삭제

s = []

push(1)
push(2)
push(3)

print("pop item =>", pop())
print("pop item =>", pop())
print("pop item =>", pop())

```

```python
# Stack
#
stack_list = []

# push
stack_list.append(1)

# peek
if len(stack_list) > 0:
    stack_list[-1]
    stack_list[len(stack_list)-1]

# pop (공백 검사 후 꺼내야 한다)
if len(stack_list) > 0:
    stack_list.pop()
    stack_list.pop(-1)
    stack_list.pop(len(stack_list)-1)




# 일반적인 언어에서 배열을 이용하여 사용한 경우는?

stack_arr = [0] * 1000000
top = -1 # 마지막 인덱스를 가리킨다.

# push ( 가득차 있는지 검사하자)
if len(stack_arr) - 1 > top:  # 길이가 넘는지 확인
    # 입맛대로 만들자
    top += 1
    stack_arr[top] = 1 # 값을 집어넣는다.

# peek 공백검사후 확인
if top >= 0:
    stack_arr[top]

# pop 공백검사후 확인
if top >= 0:
    N = stack_arr[top]
    top -= 1
```



```python
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
```



```python
# 스택1

def dfs(s, V):
    visited = [0] * (V + 1)
    stack = []
    i = s # 현재 방문한 정점 i
    visited[i] = 1
    print(node[i])
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
```



```python
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

```



```python
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
```



```python
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
​
```





## 2. 재귀함수로 피보나치 만들기

```python
# 재귀함수로 피보나치 만들기

def fibo(n):
    if n < 2:
        return n
    else:
        return fibo(n-1) + fibo(n-2)
```

```python
def f(N):
    global cnt
    cnt += 1
    memo[N] += 1
    if N < 2:
        return N

    return f(N-1) + f(N-2)

cnt = 0
memo = [0] * 20
print(f(15), cnt)
print(memo)
```





## 3. memoization을 이용한 알고리즘

```python
# memoization을 이용한 알고리즘

def fibo1(n):
    global memo
    if n >= 2 and len(memo) <= n :
        memo.append(fibo1(n-1) + fibo1(n-2))
    return memo[n]

memo = [0, 1]
```

```python
# 메모이제이션

def fibo2(n):
    pass
    global cnt
    cnt += 1
    if n >= 2 and memo2[n] == 0:
        memo2[n] = fibo2(n-1) + fibo2(n-2)
    return memo2[n]

n = 50
memo2 = [0] * (n+1)
memo2[0] = 0
memo2[1] = 1
cnt = 0
print(fibo2(n), cnt)

```







## 4. DP동적계획법을 적용한 피보나치

```python
# DP동적계획법을 적용한 피보나치 수

def fibo2(n):
    f = [0, 1]

    for i in range(2, n+1):
        f.append(f[i-1] + f[1-2])
    return f[n]
```

```python
def f(n):
    table[0] = 0
    table[1] = 1
    for i in range(2, n+1):
        table[i] = table[i-1] + table[i-2]

    return table[n]

n = int(input())
table = [0] * (n+1)

print(f(n))
```







## 5. DP동적계획법을 적용한 팩토리얼

```python
def fact(n):
    table[0] = 1
    for i in range(1, n+1):
        table[i] = i * table[i-1]

    return table[n]

n = int(input())
table = [0] * (n+1)
print(fact(n))
```



