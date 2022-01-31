subway = ['빵', '치즈', '스테이크']

n = len(subway)

for i in range(1<<n):  # 2**N 같다. 부분집합갯수
    for j in range(n):
        # 컴퓨터가 이해하는 과정은 j가 0000 0001 0010 0011
        # 이것을 미는 방법은 1<<j 이것은 2배해주는 거다
        if i & (1<<j): # 각각의 비트를 j번 민다.
            print(subway[j], end = ',')

    print()
