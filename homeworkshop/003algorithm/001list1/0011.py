# 디버깅 사용방법

def my_print(idx, N):
    print("#{}까지의 합은 {} 이다.".format(idx, N))

def my_sum(N):
    tmp = 0
    for i in range(N+1):
        tmp += i
        my_print(i, tmp)
    return tmp

ans = my_sum(10)

print(ans)

# 1. 도대체 어디에 breakpoint를 찍어야하는가
'''
step over는 뭐고
step into는 뭐고
stop out은 무엇인지 알고 사용하자

내가 원하는 곳부터 시작가능
중간중간 내가 보고싶은 변수를 이용해 결과도 볼 수 있다.
'''