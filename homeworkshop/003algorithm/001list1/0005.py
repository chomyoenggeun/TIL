# 반복문을 이용한 이진검색

def binarySearch(a, key):
    start = 0   # 인덱스
    end = len(a)-1   # 인덱스
    while start <= end :
        middle = (start + end) // 2
        if a[middle] == key:    # 찾는값과 중간값이 같다면 인덱스 출력
            return middle
        elif a[middle] > key:    # 중간값이 찾는값보다 크면 인덱스를 줄인다
            end = middle -1
        else:
            start = middle +1   # 중간값이 찾는값보다 작으면 인덱스를 더한다.
    return -1

arr = [2,4,7,9,11,19,23]
print(binarySearch(arr, 11))
print(binarySearch(arr, 10))



#  재귀 함수를 이용한 이진검색

def binarySearch2(a, low, high, key):
    if low > high:
        return False
    else:
        middle = (low+high)//2
        if key == a[middle]:
            return True
        elif key < a[middle]:
            return binarySearch2(a, low, middle-1, key)
        elif a[middle] < key:
            return binarySearch2(a, middle+1, high, key)
