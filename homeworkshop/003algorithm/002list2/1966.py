# 숫자를 정렬하자

# 5가지 정렬 방법.
#
# 1. 선택정렬
#
# 2. 버블정렬
#
# 3. 삽입정렬
#
# 4. 퀵정렬
#
# 5. 병합정렬


# 선택정렬. 앞에서부터 최솟값을 찾아 swap 시킨다.
def sort_arr(arr):
    for i in range(N-1):
        min_value = float('inf')
        min_idx = 0
        for j in range(i,N):
            if arr[j] < min_value:
                min_value = arr[j]
                min_idx = j
        arr[i], arr[min_idx] = arr[min_idx], arr[i]
    return arr


for test in range(1, int(input())+1):
    N = int(input())
    init_arr = list(map(int, input().split()))
    sorted_arr = sort_arr(init_arr)
    print(f'#{test}', end=' ')
    print(*sorted_arr)



# 버블정렬. 끝부터 범위를 하나씩 줄여가며 앞뒤로 스왑시킨다. 스왑이 일어나지 않으면 정렬 완료.
def sort_arr(N, arr):
    for i in range(N-2, -1, -1):
        swap = 0
        for j in range(0, i+1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
                swap = 1
        if not swap:
            return arr
    return arr


for test in range(1, int(input())+1):
    N = int(input())
    init_arr = list(map(int, input().split()))
    sorted_arr = sort_arr(N, init_arr)
    print(f'#{test}', end=' ')
    print(*sorted_arr)




# 삽입 정렬. 순서대로 하나씩 빼서 내 앞에 있는 애들이랑 비교. 나보다 작은애 만나면 그 뒤에 삽입.
def sort_arr(N, arr):
    for i in range(1, N):
        tmp = i
        for j in range(i-1, -1, -1):
            if arr[tmp] < arr[j]:
                arr[tmp], arr[j] = arr[j], arr[tmp]
                tmp -= 1
            else:
                break
    return arr


for test in range(1, int(input())+1):
    N = int(input())
    init_arr = list(map(int, input().split()))
    sorted_arr = sort_arr(N, init_arr)
    print(f'#{test}', end=' ')
    print(*sorted_arr)





# 삽입 정렬. 순서대로 하나씩 빼서 내 앞에 있는 애들이랑 비교. 나보다 작은애 만나면 그 뒤에 삽입.
def sort_arr(N, arr):
    for i in range(1, N):
        tmp = i
        for j in range(i-1, -1, -1):
            if arr[tmp] < arr[j]:
                arr[tmp], arr[j] = arr[j], arr[tmp]
                tmp -= 1
            else:
                break
    return arr


for test in range(1, int(input())+1):
    N = int(input())
    init_arr = list(map(int, input().split()))
    sorted_arr = sort_arr(N, init_arr)
    print(f'#{test}', end=' ')
    print(*sorted_arr)





# 퀵 정렬 : 정렬기준인 pivot 을 통해 좌우 범위로 나눠 정렬하고 합치는 정렬.
def sort_arr(arr):
    length = len(arr)
    if length <= 1:
        return arr
    middle = length//2
    pivot = arr[middle]     # pivot 은 정렬되지 않는 배열의 중앙값이며 대소비교의 기준입니다.
    rest = arr[:middle] + arr[middle+1:]    # pivot 과 비교할 모집단입니다.
    left_arr = [i for i in rest if i <= pivot]      # pivot 보다 작은 수들의 집합입니다.
    right_arr = [i for i in rest if i > pivot]      # pivot 보다 큰 수들의 집합입니다.
    return sort_arr(left_arr) + [pivot] + sort_arr(right_arr)      # 정렬이 끝났으면 다시 합칩니다.


for test in range(1, int(input())+1):
    N = int(input())
    init_arr = list(map(int, input().split()))
    sorted_arr = sort_arr(init_arr)
    print(f'#{test}', end=' ')
    print(*sorted_arr)



# 앞에서 부터 비교해 작은 숫자부터 새로운 배열에 병합합니다.
# 연산이 끝나면 정렬된 배열 merged 가 반환됩니다.
def merge(left, right):
    merged = []
    while left or right:
        if not left:
            merged += right
            return merged
        elif not right:
            merged += left
            return merged

        if left[0] < right[0]:
            merged += [left[0]]
            left = left[1:]
        else:
            merged += [right[0]]
            right = right[1:]
    return merged


# 병합 정렬 : 분할 정복을 이용한 정렬. 퀵정렬이 pivot을 기준으로 한다면 얘는 그냥 무지성 반갈.
# 반갈을 1개씩 남을때까지 한 다음 다시 병합하는데 맨앞부터 비교해서 작으면 앞에 놓는 식.
def sort_arr(arr):
    length = len(arr)
    if length <= 1:
        return arr
    middle = length//2
    left_arr = sort_arr(arr[:middle])
    right_arr = sort_arr(arr[middle:])
    return merge(left_arr, right_arr)


for test in range(1, int(input())+1):
    N = int(input())
    init_arr = list(map(int, input().split()))
    sorted_arr = sort_arr(init_arr)
    print(f'#{test}', end=' ')
    print(*sorted_arr)














# 카운팅 정렬방식

T = int(input())

for test_case in range(1, T + 1):
    N = int(input())
    nums = list(map(int, input().split()))

    # 정렬하기
    sort_nums = [0] * N
    # K = max(nums)
    # print(K)

    K = -1
    for i in nums:
        if K > i:
            K = i
    # print(K)

    # print(nums)
    # 카운팅 정렬에 필요한것 , 카운팅 리스트와 nums 리스트는 다르다.
    # K라는 값은 주어진 nums에서 가장 큰 값이다.
    counts = [0] * (K + 1)

    # 카운팅하기
    for i in range(len(nums)):
        counts[nums[i]] += 1

    # 누적합 N+1
    # for i in range(len(counts)): 아래와 같다
    for i in range(1, len(counts)):
        counts[i] += counts[i-1]  # 0부터 안되는 이유는 앞에서부터 더하기 때문이다


    # 뒤에서부터 nums를 읽어오면서 자리에 맞게 받아온다
    for i in range(len(nums)-1, -1, -1):   # 뒤에서부터 넣는 이유는 원순서를 지키기 위해서
        # 위치를 찾아보자
        # counts[nums[i]] -= 1
        # idx = counts[nums[i]]
        #
        # sort_nums[idx] = nums[i]

        # 책이랑 비교해보자, 교수님꺼랑도 비교해보자
        # n =nums[i]
        # counts[n] -= 1
        # idx = counts[n]
        # sort_nums[idx] = n

        # 교재버전
        sort_nums[counts[nums[i]] -1] = nums[i]
        counts[nums[i]] -= 1

    print("#{} {}".format(test_case, sort_nums))


# 교수님답

for i in range(1, int(input()) + 1):
    N = input()

    card = list(map(int, input()))
    # print(card)
    counting = [0] * 10

    cnt = 0 #카드 번호
    max_value = 0 #카드 갯수

    max_count = 0
    ans_idx = -1
    #카운팅을 했다...
    for k in card:
        counting[k] += 1
######################################################################################
#이 부분은 한번 충분히 생각해 볼것
        if counting[k] >= max_count:
            max_count = counting[k]
            ans_idx = k

    print(ans_idx, max_count)
    # 요거 되나안되나??????????
    # for j in range(len(counting)-1,-1,-1):
    #     if counting[j] == max_count:
    #         max_value = counting[j]
    #         cnt = j
    #         break

###################################################################################


    # for j in range(len(counting) - 1, -1, -1):
    #     #요기에 등호는 앞에서부터 접근했다면 필요함.
    #     #뒤에서부터 했으니 필요없음..
    #     if counting[j] > max_value:
    #         max_value = counting[j]
    #         cnt = j

    # print('#{} {} {}'.format(i, cnt, max_value))
