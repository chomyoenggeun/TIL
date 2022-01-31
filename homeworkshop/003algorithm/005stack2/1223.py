# 계산기2

import sys
sys.stdin = open("input2.txt", "r")


# 들어오는 입력값을 확인하며 후위연산으로 바꿔준다.
#
# 후위연산으로 만들기 위해서 숫자를 저장하는 스택과 연산자를 저장하는 스택을 운영한다.
#
# 숫자가 나온다면 숫자스택에 넣어주고
#
# 연산자가 나온다면 연산자스택의 이전값의 우선순의를 보고 판단하여 계산한다.
#
# 후위연산을 위한 분리와 계산이 끝났다면 남은 연산자를 하나의 스택으로 합쳐준다.
#
# 이제 하나의 스택의 데이터를 꺼내며 후위연산을 마무리한다.
#
# 스택에 남아있는 값이 리턴할 결과값이 된다.



# 우선순위 표기
operator = {'(' : 4, ')' : 4, '+' : 3, '-' : 3, '*' : 2, '/' : 2}

def cal(num1, num2, t): # 사칙연산 함수
    num1 = int(num1)
    num2 = int(num2)
    if t == '+':
        return num1 + num2
    elif t == '-':
        return num1 - num2
    elif t == '*':
        return num1 * num2
    elif t == '/':
        return num1 // num2


T = 10
for tc in range(1, T+1):
    input()
    arr = list(input())
    # print(arr)

    stack_operater = []  # 사칙연산 담아둘 스택
    stack_num = [] # 정수값 담아둘 스택

    for t in arr:
        # 숫자면 넣는다
        if '0' <= t <= '9':
            # print(t)
            stack_num.append(t)
        # 열린 괄호이거나 스택이 비었거나 스택 탑이 열린 괄호면 연산자를 넣는다
        elif t == '(' or not len(stack_operater) or stack_operater[-1] == '(':
            stack_operater.append(t)
        # 들어온 연산자가 우선순위가 높다면 추가( 낮은수가 높음)
        elif operator[t] < operator[stack_operater[-1]] and t != ')':
            stack_operater.append(t)
        else:
            # 위의 내용이 아니고
            # 스택이 비지않거나 들어온 연산자가 탑보다 크거나 같을때
            while len(stack_operater) and operator[t] >= operator[stack_operater[-1]]:
                # 닫는 괄호라면 괄호를 없애고 정지한다
                if stack_operater[-1] == '(':
                    stack_operater.pop()
                    break
                # 위의 조건에 해당하지 않으면 정수 스택에 추가한다.
                stack_num.append(stack_operater.pop())
            # 반복이 끝난 후 닫는 괄호가 아니면 연산자 스택에 추가
            if t != ')':
                stack_operater.append(t)
    # 남은 연산자를 처리한다
    while len(stack_operater):
        # 스택이 빌때까지 결과스택에 넣어준다.
        result = stack_operater.pop()
        if result != '(':
            stack_num.append(result)

    # 후위연산 스택을 순회하면서 확인한다
    for t in stack_num:
        # 숫자라면 임시저장
        if '0' <= t <= '9':
            stack_operater.append(t)
        else:
            #연산자라면 2개를 꺼내서 계산한다.
            num2 = stack_operater.pop()
            num1 = stack_operater.pop()
            stack_operater.append(cal(num1, num2, t))
    else:
        #결과값 출력
        print('#{} {}'.format(tc, stack_operater[0]))

