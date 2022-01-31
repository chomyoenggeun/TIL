# 열 우선 순회

arr = [
    [0, 1, 2, 3],
    [4, 5, 6, 7],
    [8, 9, 10, 11]
]

for j in range(len(arr[0])):
    for i in range(len(arr)):
        print(arr[i][j], end = ' ')

# 0 4 8 1 5 9 2 6 10 3 7 11 

# 0
# 4
# 8
# 1
# 5
# 9
# 2
# 6
# 10
# 3
# 7
# 11