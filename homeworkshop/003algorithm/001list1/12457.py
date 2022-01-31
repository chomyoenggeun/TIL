nums = [1,2,3,5,5,5]

is_ok = False

# 완전탐색을 반복문으로 푸는법
for i in range(6):
    for j in range(6):
        if j != i:
            for k in range(6):
                if k != j and k != i:
                    for l in range(6):
                        if l != k and l != j and l != i:
                            for m in range(6):
                                if m != l and m != k and m != j and m != i:
                                    for n in range(6):
                                        if n != m and n != l and n != k and n != j and n != i:
                                            print(nums[i], nums[j], nums[k], nums[l], nums[m), nums[n])
                                            left = False
                                            right = False
                                            
                                            # 왼쪽을 tir, run 검사를 해보자
                                            if nums[i] == nums[j] and nums[i] == nums[k]:
                                                left = True
                                            elif nums[i] == nums[j]-1 and nums[i] == nums[k]-2:
                                                left = True
                                            
                                            # 오른쪽도 작성하고
                                            if left and right:
                                                is_ok = True
                                                #baby gin이야
                                        



# test_case = int(input())  # Test Case 갯수
# num = int(input())  # Baby Gin 확인할 수
#
# c = [0] * 12 # 각 자리 수를 추출하여 누적할 리스트
#
# for i in range(6):   # 카드 6장을 보자
#     c[num % 10] += 1
#     num //= 10
#     print(c, num)
#
# i = 0
# triplet = dadada = 0
#
# while i < 10:
#     if c[i] > 3: # triplet 데이터 삭제
#         c[i] -= 3
#         triplet += 1
#         continue;
#     if c[i] >= 1 and c[i+1] >= 1 and c[i+2] >= 1: # dadada 조사 후 데이터 삭제
#         c[i] -= 1
#         c[i+1] -= 1
#         c[i+2] -= 1
#         dadada += 1
#         continue
#     i += 1
# if dadada + triplet == 2:
#     print("#{0} {1}".format(test_case, 1))
# else:
#     print("#{0} {1}".format(test_case, 0))
