def itoa(int_input: int) -> str:
    ans = ''
    tmp = int_input

    # 이와 같이 작성하면 값이 뒤집어져서 나온다.
    while tmp > 0:
        num = tmp % 10
        # 앞에서 접근하면 어떻게 해야할까?
        ans += chr(num + 48)

        #  뒤에서 접근하면 된다.
        # ans = chr(num + 48) + ans
        tmp //= 10
    return ans

text = itoa(1234)

print(type(text), text)