# List1

**1차원 List의 개념을 통해서 다양한 알고리즘을 공부**





### 1.정렬(Sort)

#### 	1-(1) 버블정렬

```python
# 버블정렬

def bubbleSort(arr):
    for i in range(len(arr)-1, 0, -1):  # N-1 인덱스로 밀어넣을거다
        for j in range(0, i): # 0부터 i까지 돌거다
            if arr[j] > arr[j+1]: # 앞의 자리가 크면
                arr[j], arr[j+1] = arr[j+1], arr[j] # 위치를 바꿔야지
```





#### 	1-(2) 카운트 정렬

```python
def CountingSort(A, B, K)
# A[] : 입력 리스트
# B[] : 정렬 리스트
# C[] : 카운트 리스트

C = [0] * K

    for i in range(0, len(B)):
        C[A[i]] += 1  # 입력리스트 인덱스의 값을 카운트

    for i in range(1, len(C)):
        C[i] += C[i-1]  # 누적 값 계산

    for i in range(len(B)-1, -1, -1): # 뒤로 밀어 넣겠다
        B[C[A[i]]-1] = A[i]  # 입력 인덱스에 대한 카운트값을 1씩 줄이고 정렬리스트 값을 입력 인덱스에 대한 값으로 바꿈
        C[A[i]] -= 1  # 입력 인덱스에 대한 값을 카운트 -1 

a = [0, 4, 1, 3, 1, 2, 4, 1]
b = [0] * len(a)

CountingSort(a, b, 5)
print(b)
```

```python
def Counting_Sort(A, B, k):
# A[] 입력배열
# B[] 정렬된 배열
# C[] 카운트 배열

    C = [0] * k

    for i in range(0, len(A)):
        C[A[i]] += 1

    for i in range(1, len(C)):
        C[i] += C[i-1]

    for i in range(len(B)-1, -1, -1):
        B[C[A[i]]-1] = A[i]
        C[A[i]] -= 1

```

```python
T = int(input())

for tc in range(1, T + 1):
    N = int(input())
    nums = list(map(int, input().split()))
    # 정렬하기
    sort_nums = [0] * N
    K = -1
    for i in nums:
        if K < i: K = i
    # K = max(nums)
    # 카운팅 정렬 할때 필요한게 어떤게 있었나???
    # K라는 값은 주어진 nums에서 가장 큰 값 이라고 했죠?
    counts = [0] * (K + 1)

    # 카운팅 하기
    for i in range(len(nums)):
        counts[nums[i]] += 1

    # 누적합 counts 리스트
    for i in range(1, len(counts)):
        counts[i] += counts[i - 1]


    # 뒤에서 부터 nums를 읽어오면서 자리에 맞게끔 쇽쇽쓱싹쇽
    for i in range(len(nums) - 1, -1, -1):
        # 위치를 찾아보자.
        n = nums[i]
        counts[n] -= 1
        idx = counts[n]
        sort_nums[idx] = n

        # 교재버전
        # sort_nums[counts[nums[i]]-1] = nums[i]
        # counts[nums[i]] -= 1

    print("#{} {}".format(tc, sort_nums))
```









#### 	2. 탐욕알고리즘(그리디) - 순열 생성

```python
# 순열 생성

for i1 in range(1, 4):
    for i2 in range(1, 4):
        if i2 != i1:
            for i3 in range(1, 4):
                if i3 != i1 and i3 != i2:
                    print(i1, i2, i3)
                    
                                       
# 1 2 3
# 1 3 2
# 2 1 3
# 2 3 1
# 3 1 2
# 3 2 1
```

```python
# 베이비진 완전탐색

# 크기 6인 배열의 baby-jin  여부 판단하기
arr = [5, 5, 5, 4, 4, 4]
isOk = False
for i in range(6):
    for j in range(6):
        if i != j:
            for k in range(6):
                if k != i and k != j:
                    for l in range(6):
                        if l != i and l != j and l != k:
                            for m in range(6):
                                if m != i and m != j and m != k and m != l:
                                    for n in range(6):
                                        if n != i and n != j and n != k and n != l and n != m:
                                            print(arr[i], arr[j], arr[k], arr[l], arr[m], arr[n])
                                            left = False    # 앞쪽 세개에 대한   run/triplet 결과 저장
                                            right = False     # 뒤쪽 세개에 대한   run/triplet 결과 저장
                                            # 앞 세개 인덱스, 뒤 세개 인덱스가
                                            # 각각 run  또는  triplet인지 판단
                                            if arr[i] == arr[j] and arr[i] == arr[k]:
                                                left = True
                                            elif arr[i] == arr[j]-1 and arr[i] == arr[k]-2:
                                                left = True

                                            if arr[l] == arr[m] and arr[l] == arr[n]:
                                                right = True
                                            elif arr[l] == arr[m]-1 and arr[l] == arr[n]-2:
                                                right = True

                                            if left and right:
                                                isOk = True
                                                #print("베이비진!")
if isOk:
    print("베이비진!")
else:
    print("꽝!")

```

```python
# 베이비진 탐욕

# import sys
# sys.stdin = open("sample_input.txt", "r")

T = int(input())

for tc in range(1, T+1):
    pass
    #작성해볼것!!!!

    # print("#{} {}".format(tc, ans))


num = 456799  # Baby Gin 확인할  6자리 수
c = [0] * 12  # 6자리 수로부터 각 자리 수를 추출하여 개수를 누적할 리스트


#아래의 방식은 될수도 있고 안될수도 있음.
for i in range(6):
    c[num % 10] += 1
    num //= 10

i = 0
tri = run = 0
while i < 10:
    if c[i] >= 3:  # triplet 조사 후 데이터 삭제
        c[i] -= 3
        tri += 1
        continue
    if c[i] >= 1 and c[i + 1] >= 1 and c[i + 2] >= 1:  # run 조사 후 데이터 삭제
        c[i] -= 1
        c[i + 1] -= 1
        c[i + 2] -= 1
        run += 1
        continue
    i += 1

if run + tri == 2:
    print("Baby Gin")
else:
    print("Lose")

```





