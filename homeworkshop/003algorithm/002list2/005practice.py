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