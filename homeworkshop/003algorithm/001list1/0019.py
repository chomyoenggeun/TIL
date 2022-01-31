# 퀵정렬

array = [5, 7, 9, 0, 3, 1, 6, 2, 4, 8]

def quickSort(array, start, end):
    if start >= end: # 원소가 1개인 경우 종료
        return

    pivot = start # 피벗이라는 첫 번째 원소
    left = start + 1
    right = end

    while left <= right : # 왼쪽값이 끝값보다 작으면
        # 피벗보다 큰 데이터를 찾을 때까지 반복 # 큰 그룹
        while left <= end and array[left] <= array[pivot]:
            left += 1
        # 피벗보다 작은 데이터를 찾을 때까지 반복 # 작은 그룹
        while right > start and array[right] >= array[pivot]:
            right -= 1
        if left > right: # 엇갈렸다면 작은 데이터와 피벗을 교체
            array[right], array[pivot] = array[pivot], array[right]
        else: # 엇갈리지 않았다면 작은 데이터와 큰 데이터를 교체
            array[left], array[right] = array[right], array[left]

    # 분할 이후 왼쪽 부분과 오른쪽 부분에서 각각 정렬 수행
    quickSort(array, start, right -1)
    quickSort(array, right + 1, end)

quickSort(array, 0, len(array) - 1)
print(array)