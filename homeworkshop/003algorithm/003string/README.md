# String





### 1. 고지식한 패턴 검색 알고리즘

```python 
# 고지식한 알고리즘(BruteForce)

p = 'is' # 찾을 패턴
t = 'This is a book~!' # 전체 텍스트
M = len(p) # 찾을 패턴의 길이
N = len(t) # 전체 텍스트의 길이

def BruteForce(p, t):
    i = 0 # t의 인덱스
    j = 0 # p의 인덱스
    while j < M and i < N:
        if t[i] != p[j]:
            i = i -j
            j = -1
        i = i + 1
        j = j + 1
    if j == M: 
        return i - M # 검색성공
    else:
        return -1 # 검색 실패
```





### 2.KMP 알고리즘

```python
# Python program for KMP Algorithm
def KMPSearch(pat, txt):
    M = len(pat)
    N = len(txt)
  
    # create lps[] that will hold the longest prefix suffix 
    # values for pattern
    lps = [0]*M
    j = 0 # index for pat[]
  
    # Preprocess the pattern (calculate lps[] array)
    computeLPSArray(pat, M, lps)
  
    i = 0 # index for txt[]
    while i < N:
        if pat[j] == txt[i]:
            i += 1
            j += 1
  
        if j == M:
            print ("Found pattern at index " + str(i-j))
            j = lps[j-1]
  
        # mismatch after j matches
        elif i < N and pat[j] != txt[i]:
            # Do not match lps[0..lps[j-1]] characters,
            # they will match anyway
            if j != 0:
                j = lps[j-1]
            else:
                i += 1
  
def computeLPSArray(pat, M, lps):
    len = 0 # length of the previous longest prefix suffix
  
    lps[0] # lps[0] is always 0
    i = 1
  
    # the loop calculates lps[i] for i = 1 to M-1
    while i < M:
        if pat[i]== pat[len]:
            len += 1
            lps[i] = len
            i += 1
        else:
            # This is tricky. Consider the example.
            # AAACAAAA and i = 7. The idea is similar 
            # to search step.
            if len != 0:
                len = lps[len-1]
  
                # Also, note that we do not increment i here
            else:
                lps[i] = 0
                i += 1
  
txt = "ABABDABACDABABCABAB"
pat = "ABABCABAB"
KMPSearch(pat, txt)
  
```



```python
def kmpSearch(H, N):
    n = len(H)
    m = len(N)
    # 결과값 리스트
    ret = []
    # pi[i]는 N[~i]의 접두사도 되고 접미사는 되는 문자열의 최대 길이
    pi = getPartialMatch(N)
    begin = 0
    matched = 0
    while begin <= n - m:
        # 글자가 일치한다면
        if matched < m and H[begin + matched] == N[matched]:
            matched += 1
            # m글자가 모두 일치한다면
            if matched == m:
                ret.append(begin)
        else:
            # matched가 0인 경우 다음 칸에서 시작
            if matched == 0:
                begin += 1
            else:
                begin += matched - pi[matched - 1]
                matched = pi[matched - 1]
    return ret


def getPartialMatch(N):
    m = len(N)
    pi = [0] * m
    # KMP로 N에서 N을 찾는다 (begin은 1부터)
    begin = 1
    matched = 0
    # 비교할 문자가 N의 끝에 도달할 때까지 부분 일치를 모두 기록
    while begin + matched < m:
        if N[begin + matched] == N[matched]:
            matched += 1
            pi[begin + matched - 1] = matched
        else:
            if matched == 0:
                begin += 1
            else:
                begin += matched - pi[matched - 1]
                matched = pi[matched - 1]
    return pi

H = "aflkjsklfaabaabacdsfwdsfaba"
N = "aabaabac"

print(kmpSearch(H, N)) # output : [9]
```







### 3. 보이어-무어 알고리즘

```python

# 문자열 검색하는 보이어 무어 알고리즘
def boyer_moore(pattern, text):
    # 길이를 자주쓰므로 길이를 받아둔다.
    M = len(pattern)
    N = len(text)
    i = 0
    # 반복은 최대 긴텍스트 길이 - 작은텍스트 길이
    while i <= N - M:
        # 보이어 무어 알고리즘은 뒤에서부터 접근하므로 pattern길이의 -1을 해준다.
        # -1을 해주는 이유는 인덱스가 0부터 시작하기 때문이다.
        j = M - 1
        # 뒤에서부터 검사하고 인덱스를 감소하는 형식이므로 0보다 이상일때만 동작한다.
        while j >= 0:
            # 끝글자부터 비교하면서 같다면 하나씩 감소하면서 비교한다.
            if pattern[j] != text[i + j]:
                # 글자가 틀리다면 제일마지막 글자 기준으로 find 함수를 호출한다.
                move = find(pattern, text[i + M - 1])
                break
        j = j - 1
    # 인덱스가 -1이라는 뜻은 모든 글자가 맞았다는 이야기이다.
    if j == -1:
        # 찾았으므로 true를 리턴한다.
        return True
        # 인덱스 위치를 찾는다면
        # return i
    else:
        # -1이 아니라면 글자를 못찾은 것이므로 find에서 넘겨준 값만큼 옆으로 이동한다.
        i += move


# 여기까지 왔다면 끝까지 찾지 못한것이므로 False를 리턴한다.
return False


# 인데스 위치로 한다면

# 불필요한 비교를 건너뛰기 위한 함수
def find(pattern, char):
    # 마지막 부분과 일치하는 부분이 있는지 검색한다.
    # 마지막 부분은 이미 가능성이 없으므로 그전부터 검사한다.
    for i in range(len(pattern) - 2, -1, -1):
        # 마지막글자와 패턴중 일치하는 숫자가 있다면 그만큼 이동한다.
        if pattern[i] == char:
            return len(pattern) - i - 1
    # 일치하는 글자가 없다면 패턴의 길이만큼 이동한다.
    return len(pattern)
# return -1
```

