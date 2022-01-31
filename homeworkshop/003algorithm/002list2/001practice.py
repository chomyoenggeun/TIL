# list 순회 - 행 우선 순회

arr = [
    [0, 1, 2, 3],
    [4, 5, 6, 7],
    [8, 9, 10, 11]
]

n = len(arr)     # 행의 좌표
m = len(arr[0])  # 열의 좌표

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