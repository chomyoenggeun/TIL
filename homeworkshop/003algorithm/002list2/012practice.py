# 셀렉션 알고리즘

# k번째로 작은 원소를 찾는 알고리즘

def select(list, k):
    for i in range(0, k):
        minindex = i
        for j in range(i+1, len(list)):
            if list[minindex] > list[j]:
                minindex = j
        list[i], list[minindex] = list[minindex], list[i]
    return list[k-1]