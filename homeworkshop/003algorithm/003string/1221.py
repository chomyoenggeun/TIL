# # GNS
import sys
sys.stdin = open("GNS_test_input.txt", "r")


# print(type(alpha1))
# print(alpha["TWO"])

T = int(input())
# T = 10
for test_case in range(1, T+1):
    N = list(input().split())
    # print(N)
    arr = list(input().split())
    # print(arr)
    count = len(arr)
    # print(count)

    # 딕셔너리로 키와 값을 매칭시킬거다
    alpha = {'ZRO': 0, 'ONE': 1, 'TWO': 2, 'THR': 3, 'FOR': 4, 'FIV': 5, 'SIX': 6, 'SVN': 7, 'EGT': 8, 'NIN': 9}
    number = {0: 'ZRO', 1: 'ONE', 2: 'TWO', 3: 'THR', 4: 'FOR', 5: 'FIV', 6: 'SIX', 7: 'SVN', 8: 'EGT', 9: 'NIN'}
    for i in range(count):  # 인덱스범위만큼 반복문 돌리고
        arr[i] = alpha[arr[i]] # 해당 키에 대한 값을 넣는다.
        # print(arr)

    # 정렬을 위해 버블정렬할것이다  # 함수만 쓸 수 있으면 sort쓸건데
    for j in range(len(arr)-1, 0, -1):
        for k in range(0, j):
            if arr[k] > arr[k+1]:
                arr[k], arr[k+1] = arr[k+1], arr[k]
    # print(arr)

    # arr.sort()

    # 여기서 숫자 키에 맞는 값을 매칭한다
    for l in range(count):
        arr[l] = number[arr[l]]

    print("#{} {}".format(test_case, ' '.join(arr)))


# 성아영

T = int(input())
for tc in range(T):

    # 숫자의 갯수를 담을 딕셔너리
    num_dict = {"ZRO": 0, "ONE": 0, "TWO": 0, "THR": 0, "FOR": 0,
                "FIV": 0, "SIX": 0, "SVN": 0, "EGT": 0, "NIN": 0
                }
    _, N = input().split()
    input_list = input().strip().split()
    for i in range(int(N)):
        num_dict[input_list[i]] += 1

    print("#{}".format(tc + 1))
    for key, value in num_dict.items():
        for _ in range(value):
            print(key, end=" ")
    print()


# 문찬솔

standard = ["ZRO", "ONE", "TWO", "THR", "FOR", "FIV", "SIX", "SVN", "EGT", "NIN"]
for _ in range(int(input())):
    tc, n = input().split()
    numbers = input().split()

    answer = []
    for i in range(10):
        for num in numbers:
            if standard[i] == num:
                answer.append(num)
    print(tc)
    print(' '.join(answer))
    

# 양지훈

def alien():
    nums = ["ZRO", "ONE", "TWO", "THR", "FOR", "FIV", "SIX", "SVN", "EGT", "NIN"]
    for tc in range(int(input())):
        id = list(input().split())
        input_nums = list(input().split())
        ans = []
        for i in nums:  # 외계인 숫자-아라비아숫자 번역기
            for j in range(len(input_nums)):
                if input_nums[j] == i:
                    ans.append(i)  # input을 10번 돌면서 오름차순 정리
        print(id[0])
        print(*ans)


alien()


# 최명재 - 선택정렬

# 선택 정렬 코드
def selection_sort(nums):
    for i in range(0, len(nums) - 1):
        min_idx = i
        for j in range(i + 1, len(nums)):
            if nums[min_idx] > nums[j]:
                min_idx = j
        nums[i], nums[min_idx] = nums[min_idx], nums[i]


T = int(input())

for tc in range(1, T + 1):
    N, M = list(map(str, input().split()))
    str_list = list(map(str, input().split()))

    # 정렬을 위해 딕셔너리로 값을 지정해줌
    Num_dict = {
        'ZRO': 0,
        'ONE': 1,
        'TWO': 2,
        'THR': 3,
        'FOR': 4,
        'FIV': 5,
        'SIX': 6,
        'SVN': 7,
        'EGT': 8,
        'NIN': 9
    }

    # 딕셔너리의 value 값을 통해 str_list를 선택정렬
    sorted_list = []

    for i in str_list:
        for key1, value1 in Num_dict.items():
            if i == key1:
                sorted_list.append(value1)

    selection_sort(sorted_list)

    # 정렬된 str_list를 다시 문자로 변환해줌줌
    ans_list = []

    for j in sorted_list:
        for key2, value2 in Num_dict.items():
            if j == value2:
                ans_list.append(key2)
    ans = ' '.join(map(str, ans_list))

    print('#{}'.format(tc))
    print(ans)