cnt = [0]*26
s = 'aB1a'
# print(ord('A')) # 97 #98 B를 이용해서 리스트 인덱스로 활용가능
for x in s:
    if 'a' <= x <= 'z':
    # print(x)
        cnt[ord(x)-ord('a')] += 1
    elif 'A' <= x <= 'Z':
        print(x)
    elif '0' <= x <= '9':
        print('숫자')
    # print(cnt)
print(cnt)
print(chr(65))