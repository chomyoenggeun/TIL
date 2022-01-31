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