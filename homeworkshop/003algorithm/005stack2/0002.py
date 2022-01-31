# input() 문자열 한줄 통으로 입력이 된다.

a = input()
print(a, type(a))

T = int(input())

for tc in range(1, T+1):
    ans = 0
    print("#{} {}".format(tc, ans))

for tc in range(T):
    ans = 0
    print("#{} {}".format(tc+1, ans))

for tc in range(1, int(input())+1):
    ans = 0
    print("#{} {}".format(tc, ans))
