# 카운트정렬 이해해보자











# 왜 안되지?
T = int(input()) # test_case 갯수

for test_case in range(1, T+1):
    N = int(input())    # 받는 정수 갯수
    num = list(map(int, input()))  # 문자열로 받기 때문에 split이 필요없고, 리스트로 받지 않아도 된다.

    count_list = [0] * 10   # 카운팅 정렬의 개념을 모른다..
    num = 0  # 카드번호
    cnt = 0  # 카드 갯수

    for i in range(N):      # i는 인덱스를 순차적으로 보겠다
        count_list[i] += 1

    for j in range(len(count_list)-1, -1, -1):  # j는 ?
        if count_list > cnt:
            num = count_list[j]
            cnt = j

    print("#{0} {1} {2}".format(test_case, num, cnt))







# 교수님 답



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












# 성아영 - 카운팅 정렬

T = int(input())

for tc in range(T):
    card_len = int(input())
    card_list = list(map(int, input().strip()))
    card_count = [0] * 10
    cnt = 0
    for card in card_list:
        card_count[card] += 1
    max_card = 0
    max_cnt = 0

    # 뒤에서부터 탐색해 같은 갯수라도 가장 큰 카드값이 저장되도록 함.
    for idx in range(9, -1, -1):
        if card_count[idx] > max_cnt:
            max_cnt = card_count[idx]
            max_card = idx

    print("#{} {} {}".format(tc+1, max_card, max_cnt))
