text = '삼성청년소프트웨어아카데미'
#
# # 1. 뒤에서부터 읽으면서 출력하기
# for i in range(len(text)-1, -1, -1):
#     print(text[i], end = '')
# print()
#
# # 2. 슬라이싱 사용하기
# print(text[::-1])
#
# # 3. reversed 함수 사용하기
# print(''.join(reversed(text)))
#
# # 4. swap 방식 for or while
N = len(text) // 2
tmp_text = list(text)

for i in range(N):
    tmp_text[i], tmp_text[N-1-i] = tmp_text[N-1-i], tmp_text[i]
print(''.join(tmp_text))

