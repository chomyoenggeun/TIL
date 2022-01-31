# Stack
#
stack_list = []

# push
stack_list.append(1)

# peek
if len(stack_list) > 0:
    stack_list[-1]
    stack_list[len(stack_list)-1]

# pop (공백 검사 후 꺼내야 한다)
if len(stack_list) > 0:
    stack_list.pop()
    stack_list.pop(-1)
    stack_list.pop(len(stack_list)-1)




# 일반적인 언어에서 배열을 이용하여 사용한 경우는?

stack_arr = [0] * 1000000
top = -1 # 마지막 인덱스를 가리킨다.

# push ( 가득차 있는지 검사하자)
if len(stack_arr) - 1 > top:  # 길이가 넘는지 확인
    # 입맛대로 만들자
    top += 1
    stack_arr[top] = 1 # 값을 집어넣는다.

# peek 공백검사후 확인
if top >= 0:
    stack_arr[top]

# pop 공백검사후 확인
if top >= 0:
    N = stack_arr[top]
    top -= 1