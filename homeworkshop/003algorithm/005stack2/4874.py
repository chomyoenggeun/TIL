import sys
sys.stdin = open("sample_input1.txt", "r")


T = int(input())

for tc in range(1, T+1):
    arr = input().split()
    # print(arr)

    stack_num = []

    try:
        for i in arr:
            # 마침표라면 마지막값이 정답
            if i == '.':
                ans = stack_num.pop()
                if len(stack_num) != 0:
                    ans = 'error'
                break
            elif i == '+':
                stack_num.append(stack_num.pop(-2) + stack_num.pop())
            elif i == '-':
                stack_num.append(stack_num.pop(-2) - stack_num.pop())
            elif i == '*':
               stack_num.append(stack_num.pop(-2) * stack_num.pop())
            elif i == '/':
               stack_num.append(stack_num.pop(-2) // stack_num.pop())
            else:  # 숫자는 int형으로 변환
                stack_num.append(int(i))
    except:
        ans = 'error'

    print("#{} {}".format(tc, ans))



