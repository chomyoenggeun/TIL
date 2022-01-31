# 백준 1193

# 1번 접근 1/1 한칸에 3가지를 나타낸다.
# 2번 접근 홀수일때, 짝수일때를 나눈다.
# 짝수일때, 분자는 커지고 분모는 작아지고 홀수일때, 분자는 작아지고, 분모는 커지는 규칙

X = int(input())

# 시작은 1부터
line = 1
# while을 이용한 반복문
while X > line:
    X -= line  # X 값이 1씩 감소
    line += 1
    # print(X)
    # print(line)
    # a는 분자, b는 분모
    if line % 2 == 0:
        a = X    # 짝수일때, 1씩 감소
        b = line - X + 1   # 이 부분 찾는게 어려웠다. 바로 생각이 안나더라
        # print(b)
    else:
        a = line - X + 1
        b = X    # 홀수일때, 1씩 감소

print(a, '/', b, sep='')






