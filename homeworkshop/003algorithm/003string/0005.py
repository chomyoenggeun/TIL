s = list('삼성소프트웨어아카데미')
n = len(s)


print(s)
# # 1번 방법 반나눠서 바꾼다.
# for i in range(n // 2):
#     print(i)
#     # s[i] <-> s[n-1-i]
#     s[i], s[n - 1 - i] = s[n - 1 - i], s[i]
# print(s)

# # 2번 방법, 빈리스트에 거꾸로 인덱스주소에 맞는 값을 부른다.
# ans = []
# for i in range(n-1, -1, -1):
#     ans.append(s[i])
#
# print(ans)

# print(s.reverse())
# print(dir(str))

# s.swapcase

# # 3번 방법 슬라이싱
#
# print(s[::-1])

# 4번 방법 reversed 함수 사용하기


