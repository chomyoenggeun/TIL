# 비트마스킹

arr = [1, 2, 3]
N = 3

sel = [0] * N

def perm(idx, check: int):
    # if idx == N:
    if check == (1<<N) -1:
        print(sel)
        return

    for j in range(N):
        if check & (1<<j):
            continue
        sel[idx] = arr[j]
        perm(idx + 1, check | (1<<j))

perm(0, 0)
