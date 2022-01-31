# 중위 표기법 -> 후위 표기법

arr = ['(', '(', '5', '-', '2', ')', '*', '4', ')', '/', '(', '3', '+', '5', ')']

stack = []
for i in arr:
    if i == '(' or i == ')':
       stack += arr.pop(i)
    elif i == '+' or i == '-' or i == '*' or i == '/':
        stack.append(i)

