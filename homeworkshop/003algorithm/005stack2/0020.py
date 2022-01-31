def is_exist(s):
    global cnt
    for i in range(len(s)):
        for j in range(len(s[0])):
            if s[i][j] == 7:
                cnt += 1
    return print("{}개".format(cnt))


s = [
    [3, 2, 1, 7],
    [1, 2, 3, 4],
    [7, 5, 2, 1]
]

cnt = 0
is_exist(s)
