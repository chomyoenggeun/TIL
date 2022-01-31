# List2

**2차원 List의 개념을 통해서 다양한 알고리즘을 공부**





### 1. List 순회

#### 	1-(1) 행우선 순회

```python
# list 순회 - 행 우선 순회

arr = [
    [0, 1, 2, 3],
    [4, 5, 6, 7],
    [8, 9, 10, 11]
]

n = len(arr)     # 행의 좌표, 세로
m = len(arr[0])  # 열의 좌표, 가로

for i in range(len(arr)):
    for j in range(len(arr[0])):
        print(arr[i][j], end = ' ')

# 0 1 2 3 4 5 6 7 8 9 10 11

# 0
# 1
# 2
# 3
# 4
# 5
# 6
# 7
# 8
# 9
# 10
# 11
```





#### 	1-(2) 열우선 순회

```python
# 열 우선 순회

arr = [
    [0, 1, 2, 3],
    [4, 5, 6, 7],
    [8, 9, 10, 11]
]

for j in range(len(arr[0])):
    for i in range(len(arr)):
        print(arr[i][j], end = ' ')

# 0 4 8 1 5 9 2 6 10 3 7 11 

# 0
# 4
# 8
# 1
# 5
# 9
# 2
# 6
# 10
# 3
# 7
# 11
```







#### 	1-(3) 지그재그 순회

```python
# 지그재그 순회

arr = [
    [0, 1, 2, 3],
    [4, 5, 6, 7],
    [8, 9, 10, 11]
]


n = len(arr)     # 행의 좌표
m = len(arr[0])  # 열의 좌표

for i in range(len(arr)):
    # print(i)
    for j in range(len(arr[0])):
        # print(arr[i][j+((len(arr[0])-1-2*j)*(i%2))])
        print(arr[i][j+(m-1-2*j)*(i%2)], end = ' ')

        '''
        짝수번에 왼쪽방향으로 오려면 m-1-j로 만들어줘야 한다.
        하지만 식이 복잡해지므로, i%2를 통해서 식을 간단하게 만든다.
        홀수번에는 arr[i][j]가 되고 짝수번에는 arr[i][m-1-j]이 되게
        만드는 식이 arr[i][j+(m-1-j-j)*(i%2)]이다.
        '''
        
        
# 0 1 2 3 7 6 5 4 8 9 10 11 


# 0
# 1
# 2
# 3
# 7
# 6
# 5
# 4
# 8
# 9
# 10
# 11
```







#### 1-(4) 델타를 이용한 2차 List 탐색 

```python
# 델타를 이용한 2차 list 탐색

# arr[0...n-1][0...n-1] : 2차원 list


dx = [0, 0, -1, 1] #좌우상하
dy = [-1, 1, 0, 0]

for x in range(len(arr)):
    for y in range(len(arr[x])):
        for i in range(4):
            testX = x + dx[i]
            testY = y + dy[i]
            print(arr[testX][testY])
```







## 2. 전치행렬

```python
# 전치행렬

# i = len(arr)     # 행의 좌표
# j = len(arr[0])  # 열의 좌표

arr = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

for i in range(3):
    for j in range(3):
        if i < j:
            arr[i][j], arr[j][i] = arr[j][i], arr[i][j]

print(arr)      
# [[1, 4, 7], [2, 5, 8], [3, 6, 9]]      
```









## 3. zip

```python
# zip

alpha = ['a', 'b', 'c']
index = [1, 2, 3]
alpha_index = list(zip(alpha, index))
print(alpha_index)    
# [('a', 1), ('b', 2), ('c', 3)]

arr = [[1,2,3],[4,5,6],[7,8,9]]
print(list(zip(*arr)))  
# [(1, 4, 7), (2, 5, 8), (3, 6, 9)]
```











## 4. 부분집합

#### 	4-(1)부분집합1

```python
# 부분집합1

bit = [0, 0, 0, 0]
for i in range(2):
    bit[0] = i  # 0번째 원소
    for j in range(2):
        bit[1] = j # 1번째 원소
        for k in range(2):
            bit[2] = k # 2번째 원소
            for l in range(2):
                bit[3] = l # 3번째 원소
                print(bit) # 생성된 부분집합 출력


# [0, 0, 0, 0]
# [0, 0, 0, 1]
# [0, 0, 1, 0]
# [0, 0, 1, 1]
# [0, 1, 0, 0]
# [0, 1, 0, 1]
# [0, 1, 1, 0]
# [0, 1, 1, 1]
# [1, 0, 0, 0]
# [1, 0, 0, 1]
# [1, 0, 1, 0]
# [1, 0, 1, 1]
# [1, 1, 0, 0]
# [1, 1, 0, 1]
# [1, 1, 1, 0]
# [1, 1, 1, 1]
```









#### 	4-(2) 부분집합2

```python
# 부분집합2

# 1<< n: 2^n 즉, 원소가 n개일 경우
# i & (1<<j): 1 i에서 j번째 비트가 1인지 아닌지를 리턴함
arr = [3, 6, 7, 1, 5, 4]

n = len(arr)

for i in range(1<<n): # 1<<n: 부분집합의 갯수
    for j in range(n):  # 원소의 수만큼 비트를 비교함
        if i & (1<<j): # i의 j번째 비트가 1이면 j번째 원소 출력
            print(arr[j], end = ",")

    print()

# 3,
# 6,
# 3,6,
# 7,
# 3,7,
# 6,7,
# 3,6,7,
# 1,
# 3,1,
# 6,1,
# 3,6,1,
# 7,1,
# 3,7,1,
# 6,7,1,
# 3,6,7,1,
# 5,
# 3,5,
# 6,5,
# 3,6,5,
# 7,5,
# 3,7,5,
# 6,7,5,
# 3,6,7,5,
# 1,5,
# 3,1,5,
# 6,1,5,
# 3,6,1,5,
# 7,1,5,
# 3,7,1,5,
# 6,7,1,5,
# 3,6,7,1,5,
# 4,
# 3,4,
# 6,4,
# 3,6,4,
# 7,4,
# 3,7,4,
# 6,7,4,
# 3,6,7,4,
# 1,4,
# 3,1,4,
# 6,1,4,
# 3,6,1,4,
# 7,1,4,
# 3,7,1,4,
# 6,7,1,4,
# 3,6,7,1,4,
# 5,4,
# 3,5,4,
# 6,5,4,
# 3,6,5,4,
# 7,5,4,
# 3,7,5,4,
# 6,7,5,4,
# 3,6,7,5,4,
# 1,5,4,
# 3,1,5,4,
# 6,1,5,4,
# 3,6,1,5,4,
# 7,1,5,4,
# 3,7,1,5,4,
# 6,7,1,5,4,
# 3,6,7,1,5,4,
```







## 5. 순차검색

```python
# 순차검색

def sequentialSearch(a, n, key):
    i = 0
    while i < n and a[i] != key:
        i = i + 1
    
    if i < n : 
        return i
    else:
        return -1
```







## 6. 이진검색1

```python
# 이진검색1

def binarySearch(a, key):
    start = 0
    end = len(a) - 1
    while start <= end:
         # 중간값 인덱스 접근
        middle = start + (end - start) // 2 
        if key == a[middle]: 
            return True        # 검색성공
        elif key < a[middle]:
            end = middle -1
        else:
            start = middle + 1
    return False # 검색실패
```









## 7. 이진검색 - 재귀함수를 이용

```python
# 이진검색 - 재귀함수를 이용

def binarySearch2(a, low, high, key):
    if low > high: # 검색실패
        return False
    else:
        middle = (low + high) // 2
        if key == a[middle]: # 검색성공
            return True
        elif key < a[middle]:
            return binarySearch2(a, low, middle-1, key)
        elif a[middle] < key:
            return binarySearch2(a, middle+1, high, key)
```











## 8. 셀렉션 알고리즘

```python
# 셀렉션 알고리즘# k번째로 작은 원소를 찾는 알고리즘

def select(list, k):    
    for i in range(0, k):        
        minindex = i        
        for j in range(i+1, len(list)):            
            if list[minindex] > list[j]:
                minindex = j        
                list[i], list[minindex] = list[minindex], list[i]    
                return list[k-1]
```









## 9. 선택정렬

```python
# 선택정렬
def selectionSort(a):    
    for i in range(0, len(a)-1):        
        min = i        
        for j in range(i+1, len(a)):            
            if a[min] > a[j]:                
                min = j        
                a[i], a[min] = a[min], a[i]
```

```python
arr = [6, 5, 3, 8, 1, 7, 4]
N = len(arr)

#1 단계
# 최소값의 인덱스를 찾는다.
min_idx = 0 # 0번 idx를 최소값으로 가정하고 시작
for j in range(1, N): # 1번 idx부터 마지막 idx까지 반복하며 비교 시작
    if arr[min_idx]  > arr[j]:
        min_idx = j # min_idx가 비교한 값보다 크다면 min_idx는 j로 바꾼다.
arr[0], arr[min_idx] = arr[min_idx], arr[0] # min_idx가 여전히 최소라면 0번 idx와 min_idx가 0이므로 바꿔도 그대로일 것이고,
print(arr)                                  # 비교 값이 더 작다면 min_dix와 비교 값을 바꾼다.

# 첫 번째는 끝, 패턴을 찾자.

min_idx = 1 # 제일 작은게 0번 idx로 왔으니까 범위를 앞에서부터 줄여서 1번 idx를 최소값으로 가정하고 시작
for j in range(2, N): # 1번 idx와 비교하기 위해 2번 idx부터 끝까지 반복
    if arr[min_idx]  > arr[j]: # min_idx값이 비교 값보다 크다면
        min_idx = j #             min_idx를 j로 바꾼다.
arr[1], arr[min_idx] = arr[min_idx], arr[1] # 첫 번째 반복과 마찬가지로 최소값이 1번 idx라면 그대로, 비교값이 최소값이라면 바뀐다.
print(arr)

min_idx = 2 # 이전과 마찬자기로 범위를 앞에서 부터 줄여서 비교하므로 2번 idx가 가장 작다고 가정하고 시작... 반복
for j in range(3, N):
    if arr[min_idx]  > arr[j]:
        min_idx = j
arr[2], arr[min_idx] = arr[min_idx], arr[2]
print(arr)
# 이걸 N-1번 반복
# ----------------------------------------------------------------------------------------------------------------
# 위의 코드를 하나로 만들면 선택 정렬
for i in range(0, N-1): # 바깥 for문은 최소값을 가정한다. 0번째 idx부터 N-1 idx를 최소값을 가진 idx라 가정하고
    min_dix = i         # i로 하나씩 반복하면서 i의 뒤에 있는 값과 비교한다. 앞에서부터 쭉 반복했다면 최소값은 앞으로 다 왔기 때문에 마지막을 할 필요 없다. 만약 한다면 범위를 벗어난다.
    for j in range(i + 1, N): # i를 최소 값을 가진 idx라 가정했고, i + 1부터 마지막 idx인 N까지 반복하면 비교한다. i가 증가할수록 비교 범위는 앞에서부터 점점 줄어든다.
        if arr[min_idx] > arr[j]: # min_idx와 j(i + 1에서 N까지의 idx)를 비교해서 min_idx가 j보다 크다면 min_idx를 j로 바꾸고 반복
            min_idx = j
    arr[i], arr[min_idx] = arr[min_idx], arr[i]
print(arr)


```





