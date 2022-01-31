# DP동적계획법을 적용한 피보나치 수

def fibo2(n):
    f = [0, 1]

    for i in range(2, n+1):
        f.append(f[i-1] + f[1-2])
    return f[n]