# 1차 비밀지도
# 이진법

    map1 = Mybin(n, arr1)
    map2 = Mybin(n, arr2)
    answer = [""] * n

    for i in range(n):
        for j in range(n):
            # 둘다 0인 경우에만 공백백
           if map1[i][j] == '0' and map2[i][j] == '0':
                answer[i] == " "
            else: # 그 외에는 # 채우움
                answer[i] += '#'
    return answer

def MyBin(n, arr):
    ls = [] # 2진수로 바꾼 문자열 받을 리스트변수

    for i in range(n):
        mybin = '' # 2진수로 만든 문자열 받음
        num = arr[i] # 10진수 수를 따로 저장
        # 2진수로 바꾸는 반복문
        while num >= 1:
            mybin = str(num % 2) + mybin
            num //= 2

        # 길이를 n만큼 채워야 하므로, n보다 짧게 나온 문자열을 짧은 만큼의 0을 앞에 붙인다.
        if len(mybin) < n:
            mybin = (str(0) * (n - len(mybin))) + mybin
        ls.append(mybin)

    return ls




def soution(n, arr1, arr2):
    answer = []
    for i in range(n):
        # OR 연산 후 이진수 변환
        answer.append(
            bin(arr1[i] | arr2[i])[2:] # 이진수 변환이니까 2: ok
            .zfill(n)   # zfill의 뜻?
            .replace('1', '#')
            .replace('0', ' ')
        )
    return answer


# 풀어쓴거

def solution(n, arr1, arr2) :
    result = []

    for j in range(0,len(arr1)) :
        ret = ''
        num = arr1[j] | arr2[j]

        for i in range(0, n) :
            if num % 2 == 0 :
                ret = ' ' + ret

            else :
                ret = '#' + ret

            num = int(num / 2)

        result.append(ret)

    return result

# 이진법 안쓰고 한거

def solution(n, arr1, arr2):
    answer = []
    for pos in range(0, n):
        answer.append(numToMap(n, arr1[pos], arr2[pos]))
    return answer

def numToMap(n, a1, a2):
    m1 = '{a:0{d}b}'.format(a=a1, d=n) # ㅅㅂ 무슨말이지
    m2 = '{a:0{d}b}'.format(a=a2, d=n)
    res = ''
    for pos in range(0, n):
        if m1[pos] == '1' or m2[pos] == '1':
            res += '#'
        else:
            res += ' '
    return res


# 이건 뭐야
def solution(n, arr1, arr2):
    answer = []
    for i,j in zip(arr1,arr2):
        a12 = str(bin(i|j)[2:])
        a12=a12.rjust(n,'0')   # r.just?
        a12=a12.replace('1','#')
        a12=a12.replace('0',' ')
        answer.append(a12)
    return answer
