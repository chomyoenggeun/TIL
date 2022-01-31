def CountingSort(A, B, K):


# A[] : 입력 리스트
# B[] : 정렬 리스트
# C[] : 카운트 리스트

    C = [0] * K

    for i in range(0, len(B)):
        C[A[i]] += 1  # 입력리스트 인덱스의 값을 카운트

    for i in range(1, len(C)):
        C[i] += C[i - 1]  # 누적 값 계산

    for i in range(len(B) - 1, -1, -1):  # 뒤로 밀어 넣겠다
        B[C[A[i]] - 1] = A[i]  # 입력 인덱스에 대한 카운트값을 1씩 줄이고 정렬리스트 값을 입력 인덱스에 대한 값으로 바꿈
        C[A[i]] -= 1  # 입력 인덱스에 대한 값을 카운트 -1

a = [0, 4, 1, 3, 1, 2, 4, 1]
b = [0] * len(a)

CountingSort(a, b, 5)
print(b)

# 카운팅 정렬 함수

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

