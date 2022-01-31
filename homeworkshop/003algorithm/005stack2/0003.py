# 2차원 리스트 입력방법

N, M = map(int, input().split())

# 1. 빈리스트를 만들어 넣고 1차 리스트를 append 하자.

arr = []
for _ in range(N): # _ 크게 활용하는 변수가 아니라서 사용
    tmp = list(map(int, input().split()))
    arr.append(tmp)

for i in arr:
    print(*i)

# 2. 행의 공간을 미리 확보를 해두고 해당 자리를 바꾼다.

arr = [0] * N

for i in range(N):
    arr[i] = list(map(int, input().split()))

# 3. 리스트 내포 방식

arr = [list(map(int, input().split())) for _ in range(N)]

for i in arr:
    print(*i)

# N*M 크기의 0으로 가득차 2차원 배열

arr = [[0] * M for _ in range(N)]

# 정수로 안받기
maps = [list(input()) for _ in range(16)]