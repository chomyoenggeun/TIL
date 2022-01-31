# 정수 하나 입력 : input()을 하면 문자열로 입력받기 때문에 int로 감싸서 정수로 바꾼다.
int(input())

# 정수 여러개 입력 : map(적용할 함수, 적용할 값들) input 받은 값들을 공백 단위로 나누어서 정수로 바꾼 후 list로 만든다.
list(map(int, input().split()))

# 언패킹 : 입력이 몇 개 안될 때 바로 변수로 부여하면 편하다.
x, y = map(int, input().split())

# 입력
input() # 키보드로 입력한 값을 코드에 연결

# 같은 경로에 있는 파일을 입력으로 불러오는 법
import sys
sys.stdin = open('a.txt', 'r')


print(map(int, input().split()))

# abcde
# 한줄짜리 문자열을 리스트로 바꾸고 싶을때
#
# a b c d e
a = input().split()
print(a)

# 123456789

print(list(map(int, input().split(','))))


