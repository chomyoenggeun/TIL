import sys
sys.stdin = open("input2.txt", "r")

# 김도훈

T = int(input())
for tc in range(T):
    N = int(input())
    # 2차원 배열 만들어주기
    graph = [[0] * N for _ in range(N)]
    print("#{}".format(tc + 1))

    # 열이 0번이거나 행과 열이 같은 경우 1로 만들어준다. (양끝)
    for i in range(N):
        for j in range(i + 1):
            if j == 0 or i == j:
                graph[i][j] = 1
            # 아닐경우 자신위에 한칸 왼쪽과 바로 위 숫자가 더한 값이기 때문에 계산해준다.
            else:
                graph[i][j] = graph[i - 1][j - 1] + graph[i - 1][j]

    # 0일 경우에는 아무 숫자가 없기 때문에 pass 해주고 나머지 숫자는 차례대로 출력해준다.
    for i in range(N):
        for j in range(N):
            if graph[i][j] == 0:
                pass
            else:
                print(graph[i][j], end=' ')
        print()  # 다음줄로 가기 위함


# 성아영

T = int(input())

for tc in range(T):
    num = int(input())
    pascal = []

    for i in range(num):
        temp = [0] * (i + 1)

        # 첫 값, 끝 값은 항상 1
        temp[0] = 1
        temp[-1] = 1
        for idx in range(1, i):
            temp[idx] = pascal[i - 1][idx - 1] + pascal[i - 1][idx]
        pascal.append(temp)
    print("#{}".format(tc + 1))
    for i in range(num):
        print(*pascal[i])


# 안되는 방법
T = int(input())
# print(T)
for tc in range(1, T+1):
    N = int(input())
    # 1번 방법
    arr = [[0] * N for _ in range(N)] # 빈리스트
    # print(arr)
    # 2번 방법
    # arr = [[0 for col in range(10)] for row in range(10)]
    # print(arr)
    
    # 파스칼 삼각형 만들기
    for r in range(0 , N):
        for c in range(0, r+1):
            if r == 0 or r == c: # 왼쪽 삼각형 높이와 빗변이 1이라서
                arr[r][c] = 1
            else:
                arr[r][c] = arr[r-1][c-1] + arr[r-1][c] # 파스칼 특성
    # print(arr)

    # 파스칼 삼각형 0 제거
    for i in range(N):
        for j in range(N):
            if arr[i][j] == 0:
                print(" ", end = '')
            # 파스칼 삼각형 숫자만 만들고
            else:
                print(arr[i][j], end = '')
        # 출력 # 이거 때문에 늦음...
        print("\n")
            