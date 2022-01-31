# 숫자를 정렬하자

# 카운팅 정렬방식

T = int(input())

for test_case in range(1, T+1):
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
        n =nums[i]
        counts[n] -= 1
        idx = counts[n]
        sort_nums[idx] = n

        # 교재버전
        # sort_nums[counts[nums[i]] -1] = nums[i]
        # counts[nums[i]] -= 1

    print("#{} {}".format(test_case, sort_nums))
