# 델타를 이용한 2차 list 탐색

# arr[0...n-1][0...n-1] : 2차원 list


dx = [0, 0, -1, 1] #상하좌우
dy = [-1, 1, 0, 0]

for x in range(len(arr)):
    for y in range(len(arr[x])):
        for i in range(4):
            testX = x + dx[i]
            testY = y + dy[i]
            print(arr[testX][testY])