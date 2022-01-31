import sys
sys.stdin = open("sample_input1.txt", "r")

T = int(input())
for test_case in range(1, T+1):
    # 값 받기
    str1 = input()
    str2 = input()
    N = len(str1)
    M = len(str2)
    result = 0
    for i in range(M-N+1): # 인덱스 범위가 안넘게
        if str2[i:i+N] == str1:
            result = 1
    print("#{} {}".format(test_case, result))



# TC = int(input())

# for tc in range(1, TC+1):
#     str1 = input()
#     str2 = input()
#
#     result = 0
#     for i in range(len(str2)-len(str1)+1):
#         if str2[i:i+len(str1)] == str1:
#             result = 1
#
#     print('#%d %s'%(tc, result))