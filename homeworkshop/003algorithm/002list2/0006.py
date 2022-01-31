arr = [6, 5, 3, 8, 1, 7, 4]
N = len(arr)

#1 단계
# 최소값의 인덱스를 찾는다.
'''min_idx = 0 # 범위의 값은 0로 가정하고 시작
for j in range(1, N):
    if arr[min_idx]  > arr[j]:
        min_idx = j
arr[0], arr[min_idx] = arr[min_idx], arr[0]
print(arr)

# 첫 번째는 끝, 패턴을 찾자.

min_idx = 1 # 범위의 값은 0로 가정하고 시작
for j in range(2, N):
    if arr[min_idx]  > arr[j]:
        min_idx = j
arr[1], arr[min_idx] = arr[min_idx], arr[1]
print(arr)

min_idx = 2 # 범위의 값은 0로 가정하고 시작
for j in range(3, N):
    if arr[min_idx]  > arr[j]:
        min_idx = j
arr[2], arr[min_idx] = arr[min_idx], arr[2]
print(arr)'''
# 이걸 N-1번 반복


for i in range(0, N-1):
    min_dix = i
    for j in range(i + 1, N):
        if arr[min_idx] > arr[j]:
            min_idx = j
    arr[i], arr[min_idx] = arr[min_idx], arr[i]
print(arr)