# 베이비진 완전탐색

# 크기 6인 배열의 baby-jin  여부 판단하기
arr = [5, 5, 5, 4, 4, 4]
isOk = False
for i in range(6):
    for j in range(6):
        if i != j:
            for k in range(6):
                if k != i and k != j:
                    for l in range(6):
                        if l != i and l != j and l != k:
                            for m in range(6):
                                if m != i and m != j and m != k and m != l:
                                    for n in range(6):
                                        if n != i and n != j and n != k and n != l and n != m:
                                            print(arr[i], arr[j], arr[k], arr[l], arr[m], arr[n])
                                            left = False    # 앞쪽 세개에 대한   run/triplet 결과 저장
                                            right = False     # 뒤쪽 세개에 대한   run/triplet 결과 저장
                                            # 앞 세개 인덱스, 뒤 세개 인덱스가
                                            # 각각 run  또는  triplet인지 판단
                                            if arr[i] == arr[j] and arr[i] == arr[k]:
                                                left = True
                                            elif arr[i] == arr[j]-1 and arr[i] == arr[k]-2:
                                                left = True

                                            if arr[l] == arr[m] and arr[l] == arr[n]:
                                                right = True
                                            elif arr[l] == arr[m]-1 and arr[l] == arr[n]-2:
                                                right = True

                                            if left and right:
                                                isOk = True
                                                #print("베이비진!")
if isOk:
    print("베이비진!")
else:
    print("꽝!")
