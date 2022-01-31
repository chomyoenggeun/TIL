import sys
sys.stdin = open('sample_input3.txt', 'r')

# 반복문자 지우기

T = int(input())
for tc in range(1, T+1):
    # 문자열을 각각 리스트로 받는다
    arr = list(input())
    # print(arr)
    # tmp에 인덱스 0값을 추가, stack
    tmp = [arr[0]]

    for i in range(1, len(arr)):
        # 공백일 때
        if not tmp:
            tmp.append(arr[i])
        # 중복이 있으면 pop으로 제거
        elif tmp[-1] == arr[i]:  #스택과 문자열이 일치하면 제거
            tmp.pop()
        # 아니면 값추가
        else:
            tmp.append(arr[i])

    print('#{} {}'.format(tc, len(tmp)))


# 전호정

#반복문자 지우기
T=int(input())
for tc in range(1,T+1):
    s=list(input()) # 리스트로 입력  예시: ['A', 'B', 'C', 'C', 'B']
    while 1:
        for i in range(len(s)-1): # 앞에서부터 검사
            if s[i]==s[i+1]:
                s.pop(i+1) # 뒤에꺼 먼저 제거해서 i 인덱스 변화 없게
                s.pop(i)
                break
        else: # 반복문을 다 돌면 더이상 연속 반복 문자가 없다는 뜻
            break
    result=len(s)
    print('#{} {}'.format(tc,result))