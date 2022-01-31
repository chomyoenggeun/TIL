import sys
sys.stdin = open('sample_input4.txt', 'r')

T = int(input())

def check(): # check할 함수 생성
    
    for i in str1:
        # 문자열에 열린 괄호가 있다면
        if i == "{" or i == "(":
            # s에 더한다
            s.append(i)
        # 문자열에 닫힌 괄호라면
        elif i == "}" or i == ")":
            if s:
                # s에서 빼준다
                a = s.pop()
            else:
                # 그게 아니면 0리턴
                return 0
            # 근데 다른 괄호가 있으면 0리턴
            if a == "{" and i == ")":
                return 0
            # 반대 경우도 고려
            if a == "(" and i == "}":
                return 0
    # 이랬는데 아무것도 없으면 0리턴
    if s:
        return 0
    # 그외는 잘했으니까 1리턴
    else:
        return 1


for tc in range(1, T+1):
    # 문자열을 받는다
    str1 = input()
    # print(str1)
    # 빈 리스트를 만든다.
    s = []
    print("#{} {}".format(tc, check()))
