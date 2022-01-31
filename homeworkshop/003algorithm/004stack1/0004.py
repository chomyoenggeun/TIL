def f(N):
    global cnt
    cnt += 1
    memo[N] += 1
    if N < 2:
        return N

    return f(N-1) + f(N-2)

cnt = 0
memo = [0] * 20
print(f(15), cnt)
print(memo)