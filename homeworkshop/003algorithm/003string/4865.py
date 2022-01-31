import sys
sys.stdin = open("sample_input1.txt", "r")

T = int(input())
for test_case in range(1, T+1):
    str1 = input()
    str2 = input()
    # print(str1)
    # print(str2)
    cnt = 0
    max_cnt = 0
    # if str1 in str2:
    #     print(str1)
    for i in str1:
        for j in str2:
            if i == j:
                cnt += 1
        if max_cnt < cnt:
            max_cnt = cnt
        cnt = 0    #리셋 꼭 해주기
    print("#{} {}".format(test_case, max_cnt))