# 조명근

for test_case in range(1, 11):    # 10개의 소스코드가 주어진다
	N = int(input())        # 가로길이 건물수
    building = list(map(int, input().split()))      # 건물높이 리스트로 만들기

    view = 0    # 전망을 0으로 초기화
    for i in range(2, N-2):    # 두칸 떨어뜨린다.
        gap1 = building[i] - building[i-2] # 현재 위치에서 -2
        gap2 = building[i] - building[i-1] # 현재 위치에서 -1
        gap3 = building[i] - building[i+1] # 현재 위치에서 +1
        gap4 = building[i] - building[i+2] # 현재 위치에서 +2
        if gap1 > 0 and gap2 > 0 and gap3 > 0 and gap4 > 0:  # 차가 0보다만 크면 높은거다.
            view += min(gap1, gap2, gap3, gap4)   # 양 사이드에서 걸리는게 가장 작아야된다.

	print("#{0} {1}".format(test_case, view))







# 성아영

def my_max(*args):
    max_num = args[0]
    for num in args:
        if num > max_num:
            max_num = num
    return max_num


for T in range(1, 11):
    test_case = int(input())
    height = list(map(int, input().split()))
    result = 0
    for idx in range(2, test_case-2):
        max_height = my_max(height[idx-2], height[idx-1], height[idx+1], height[idx+2])
        if height[idx] > max_height:
            result += (height[idx] - max_height)

    print("#{} {}".format(T, result))



# 문찬솔

# 총 10개의 테스트 케이스
for tc in range(1, 11):
    # 총 건물의 수
    building = int(input())
    # 건물들의 층 수
    stories = list(map(int, input().split()))
    # 조망권 확보세대를 셀 변수 설정
    views = 0
    # 제일 처음 2개와 제일 끝 2개는 0층
    for i in range(2, building-1):
        # 바로 양 옆 건물들과 비교
        if stories[i] > stories[i-1] and stories[i] > stories[i+1]:
            dif1 = stories[i]-stories[i-1] if stories[i]-stories[i-1] < stories[i]-stories[i+1] else stories[i]-stories[i+1]
            # 두 칸 넘어의 건물들과 비교
            if stories[i] > stories[i-2] and stories[i] > stories[i+2]:
                dif2 = stories[i]-stories[i-2] if stories[i]-stories[i-2] < stories[i]-stories[i+2] else stories[i]-stories[i+2]
                # 건물들과의 층수 차이 중 가장 작은 수를 조망권 확보 세대로 더해준다.
                view = dif1 if dif1 <= dif2 else dif2
                views += view

    print('#{} {}'.format(tc, views))


# 전호정

def my_max(a,b):
    if a>b:
        return a
    else:
        return b


ans=[]
for i in range(10):
    l=int(input())
    total=0
    b_list=list(map(int,input().split()))

    for j in range(2,l-2):
        left_big=my_max(b_list[j-2],b_list[j-1])
        right_big=my_max(b_list[j+1],b_list[j+2])
        if b_list[j]>left_big and b_list[j]>right_big:
            total+=b_list[j]-my_max(left_big,right_big)
    ans.append(total)
    b_list.clear()

for i in range(len(ans)):
    print('#{} {}'.format(i+1,ans[i]))
