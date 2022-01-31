# 메모이제이션

def fibo2(n):
    pass
    global cnt
    cnt += 1
    if n >= 2 and memo2[n] == 0:
        memo2[n] = fibo2(n-1) + fibo2(n-2)
    return memo2[n]

n = 50
memo2 = [0] * (n+1)
memo2[0] = 0
memo2[1] = 1
cnt = 0
print(fibo2(n), cnt)
