# 피보나치 메모이제이션

def fibo2(n):
    pass
    if memo2[n] == -1:
        memo2[n] = fibo2(n-1) + fibo2(n-2)
    return memo2[n]

N = 10
memo2 = [-1] * (N+1)

memo2[0] = 0
memo2[1] = 1

print(fibo2(N))
print(memo2)