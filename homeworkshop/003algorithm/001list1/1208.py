# T = int(input()) # test_case 갯수 버블정렬을 두번 단점, break 조건

for test_case in range(1, 11):    # 10개
    N = int(input())    # 덤프 횟수
    box = list(map(int, input().split()))  # 박스 높이 리스트

    result = 0 # 결과값
    # count = 0
    for i in range(N):       # 덤프 횟수만큼 반복
        for j in range(len(box)-1, 0, -1):  # 버블정렬 이용
            for k in range(0, j):
                if box[k] > box[k+1]:
                    box[k], box[k+1] = box[k+1], box[k]
        box[0] += 1    # 최소값 +1
        box[-1] -= 1  # 최대값 -1

    for i in range(N):       # 덤프 횟수만큼 반복
        for j in range(len(box)-1, 0, -1):  # 버블정렬 이용
            for k in range(0, j):
                if box[k] > box[k+1]:
                    box[k], box[k+1] = box[k+1], box[k]

    result = box[-1] - box[0]

    print("#{} {}".format(test_case, result))




# min max 쓸때 정렬할 필요없다.

for t in range(1, 11) :  # test_case 10개
    N = int(input())    # 덤프횟수
    box = list(map(int, input().split()))   # 박스 높이

    for i in range(N):   # 덤프 횟수만큼
        max_index = box.index(max(box))   # 최대값의 인덱스 값을 돌려준다
        # print(max_index)
        min_index = box.index(min(box))   # 최소값의 인덱스 값을 돌려준다
        box[max_index] -= 1   # 최대값에 -1
        box[min_index] += 1   # 최소값에 +1

    print("#{} {}".format(t, max(box)-min(box)))



# Flatten
def Bubblesort(a):                               # 숫자 정렬 함수 설정
    for i in range(len(a) - 1, 0, -1):
        for j in range(0, i):
            if a[j] > a[j + 1]:
                a[j], a[j + 1] = a[j + 1], a[j]
    return a
 

for case in range(10):                          # 케이스 반복
    dump = int(input())                         # dump 수입력
    data = list(map(int, input().split()))      # data 입력
    for d in range(dump):                       # 덤프 만큼 반복
        Bubblesort(data)                        # 숫자를 정렬하고
        data[0] += 1                            # 제일작은수 +1
        data[-1] -= 1                           # 제일큰수 -1
 
    Bubblesort(data)                            # 최종 정렬
                                                # 마지막수 - 처음수
    print("#{} {}".format(case+1, data[-1]-data[0]))



# 성아영

# 평탄화
 
for tc in range(10):
    dump = int(input())
    height = list(map(int, input().split()))
    max_num = 0
    min_num = 100
 
    # 마지막 값까지 적용 시키기 위해 1을 더해줌
    for i in range(dump+1):
        max_num = 0
        min_num = 101
        max_idx = -1
        min_idx = -1
 
        # max, min값 찾아서 평탄화 작업
        for idx in range(100):
            if height[idx] > max_num:
                max_num = height[idx]
                max_idx = idx
            if height[idx] < min_num:
                min_num = height[idx]
                min_idx = idx
        # 만약 둘의 차이가 1이하라면 반복문 종료
        if max_num - min_num <= 1:
            break
        height[max_idx] -= 1
        height[min_idx] += 1
 
    print("#{} {}".format(tc+1, max_num - min_num))



# 양지훈

def flatten():
    for tc in range(1, 11):
        N = int(input())
        box = list(map(int, input().split()))
        for i in range(N+1):
            top, bottom = 0, 100
            for b in box:
                if top < b:
                    top = b
                if bottom > b:
                    bottom = b
            if top - bottom <= 1:
                break

            # 최대값 1칸 덜기
            for j in range(len(box)):
                if box[j] >= top:
                    box[j] -= 1
                    break

            # 최소값 1칸 더하기
            for k in range(len(box)):
                if bottom >= box[k]:
                    box[k] += 1
                    break

        print("#{} {}".format(tc, top-bottom))

flatten()





