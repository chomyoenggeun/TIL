# 재귀함수로 피보나치 만들기

def fibo(n):
    if n < 2:
        return n
    else:
        return fibo(n-1) + fibo(n-2)