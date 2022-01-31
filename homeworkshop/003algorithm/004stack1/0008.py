# 피보나치 메모이제이션

def fibo1(n):
    global memo
    if n >= 2 and len(memo) <= n:
        memo.append(fibo1(n-1) + fibo1(n-2))
    return memo[n]

memo = [0, 1]  # 기록 저장을 위해

print(fibo1(4))
print(memo)

7 8
0 1
0 2
1 3
1 4
2 4
3 5
4 5
5 6