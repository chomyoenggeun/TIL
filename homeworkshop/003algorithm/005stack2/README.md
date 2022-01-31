# Stakc2



## 1. 부분집합생성하기

```python
bit = [0, 0, 0, 0]
for i in range(2):
    bit[0] = i                  # 0번째 원소
    for j in range(2):
        bit[1] = j              # 1번째 원소
        for k in range(2):
            bit[2] = k          # 2번째 원소
            for l in range(2):
                bit[3] = l      # 3번째 원소
                print(bit)      # 생성된 부분집합 출력
```







## 2. powerset을 구하는 백트래킹 알고리즘

```python
def backtrack(a, k, input):
    glodbal MAXCANDIDATES
    c = [0] * MAXANDIDATES
    
    if k == input :
        process_solution(a, k) # 답이면 원하는 작업을 한다
    else : 
        k += 1
        ncandidates = construct_candidates(a, k, input, c)
        for i in range(ncandidates) :
            a[k] = c[i]
            backtrack(a, k, input)
```









## 3. powerset을 구하는 백트래킹 알고리즘

```python

```







## 4. 백트래킹을 이용하여 순열 구하기

```python

```







## 5. 백트래킹을 이용하여 순열 구하기

```python

```







## 6. 분할정복 예제 거듭제곱

```python

```







## 7. 분할정복 기반의 알고리즘

```python

```









## 8. 퀵정렬

```python
def quickSort(a, begin, end) :
    if begin < end :
        p = partition(a, begin, end)
        quickSort(a, begin, p-1)
        quickSort(a, p+1, end)
```







## 9. 퀵정렬

```python
def partition(a, begin, end) :
    pivot = (begin + end) // 2
    L = begin
    R = end
    while L < R :
        while(a[L] < a[pivot] and L < R) : L += 1
        while(a[R] >= a[pivot] and L < R) : R -= 1
        if L < R :
            if L == pivot : pivor = R
            a[L], a[R] = a[R], a[L]
    a[pivot], a[R] = a[R], a[pivot]
    return R
```

