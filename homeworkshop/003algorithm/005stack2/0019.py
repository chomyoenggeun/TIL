def is_exist(s):
    for i in len(s):
        if s[i] == 7:
            return 1
    
    return 0 # for문 다 돌았는데도 없다



s = [3, 2, 1, 7, 5, 9]

is_exist(s)
