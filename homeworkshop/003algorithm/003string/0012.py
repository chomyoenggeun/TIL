def atoi(str_input: str) -> int:
    ans = 0

    for i in range(len(str_input)):
        ans *= 10
        ans += ord(str_input[i]) - ord('0')
        # ord(str_input[i]) - 48
    return ans

    # 양수만을 위한 코드
    # 음수코드는 어떻게 해야할까?

num = atoi("1234")
print(type(num), num)