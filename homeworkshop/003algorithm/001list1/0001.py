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



print(map(int, input().split()))

# abcde
# 한줄짜리 문자열을 리스트로 바꾸고 싶을때
#
# a b c d e
a = input().split()
print(a)

# 123456789

print(list(map(int, input().split(','))))

# 더 중요한 것은 2차원 리스트 입력
