# 지그재그 순회

arr = [
    [0, 1, 2, 3],
    [4, 5, 6, 7],
    [8, 9, 10, 11]
]


n = len(arr)     # 행의 좌표
m = len(arr[0])  # 열의 좌표

for i in range(len(arr)):
    # print(i)
    for j in range(len(arr[0])):
        # print(arr[i][j+((len(arr[0])-1-2*j)*(i%2))])
        print(arr[i][j+(m-1-2*j)*(i%2)], end = ' ')

# 0 1 2 3 7 6 5 4 8 9 10 11 


# 0
# 1
# 2
# 3
# 7
# 6
# 5
# 4
# 8
# 9
# 10
# 11