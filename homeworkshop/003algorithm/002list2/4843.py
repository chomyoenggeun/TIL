# 특별한 정렬 - 셀렉션 알고리즘




# 양지훈

def special_sort():
    for tc in range(1, 1 + int(input())):
        length = int(input())
        arr = list(map(int, input().split()))
        for i in range(10):
            if i % 2:
                temp = i
                for j in range(i + 1, length):
                    if arr[j] < arr[temp]:
                        temp = j
                arr[i], arr[temp] = arr[temp], arr[i]
            else:
                temp = i
                for k in range(i + 1, length):
                    if arr[k] > arr[temp]:
                        temp = k
                arr[i], arr[temp] = arr[temp], arr[i]
        print("#{} {}".format(tc, " ".join(map(str, arr[:10]))))


special_sort()



# 성아영

def selection_sort(input_list):
    # 원본값을 유지하기 위해
    new_list = input_list[:]
    for i in range(len(new_list) - 1):
        min_idx = i
        for j in range(i + 1, len(new_list)):
            if new_list[j] < new_list[min_idx]:
                min_idx = j
        new_list[i], new_list[min_idx] = new_list[min_idx], new_list[i]
    return new_list


T = int(input())

for tc in range(T):
    num_len = int(input())
    num_list = list(map(int, input().split()))
    sorted_list = selection_sort(num_list)
    result_list = [0] * 10

    # 짝수 인덱스는 큰값 부터 홀수 인덱스는 작은값 부터
    even_idx = num_len - 1
    odd_idx = 0

    # 10개까지만 출력
    for i in range(10):
        if i % 2:
            result_list[i] = sorted_list[odd_idx]
            odd_idx += 1
        else:
            result_list[i] = sorted_list[even_idx]
            even_idx -= 1
    print("#{}".format(tc + 1), end=" ")
    print(*result_list)
