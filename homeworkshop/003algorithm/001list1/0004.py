# 2차원 배열 입력받기
N, M = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(N)]
print(arr)

arr2 = [[0] * M for _ in range(N)]
# arr2 = [[0]*M]*N # 사용불가
print(arr2)

arr[0][1] = 10
arr2[0][1] = 10
print(arr)
print(arr2)

# 2차원 배열 접근

print(len(arr)) # 행의 좌표, 세로길이
print(len(arr[0])) # 열의 좌표, 가로길이

# 부분집합
