p = 'is' # 찾을 패턴
t = 'This is a book~!' # 전체 텍스트
M = len(p) # 찾을 패턴의 길이 2
N = len(t) # 전체 텍스트의 길이 16

def BruteForce(p, t):
    i = 0 # t의 인덱스
    j = 0 # p의 인덱스
    while j < M and i < N:  # j 0 < 16 이고 0 < 2
        if t[i] != p[j]:   # p[j]가 아니면 t[0]
            i = i - j
            j = -1
        i = i + 1     # 맞으면 인덱스를 이동시키고
       j = j + 1
    if j == M:     # 비교 텍스트 길이와 j가 2이면
        return i - M # 검색성공
    else:
        return -1 # 검색실패