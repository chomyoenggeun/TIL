# 삽입정렬

array = [7, 5, 9, 0, 3, 1, 6, 2, 4, 8]

for i in range(1, len(array)):
    for j in range(i, 0, -1): # 정렬이 되어있다고 판단
        if array[j] < array[j-1]: # 뒤에 값이 앞에 값보다 작으면
            array[j], array[j-1] = array[j-1], array[j] # 교환
        else:
            break
print(array)