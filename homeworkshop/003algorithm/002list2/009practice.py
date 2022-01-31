# 순차검색

def sequentialSearch(a, n, key):
    i = 0
    while i < n and a[i] != key:
        i = i + 1
    
    if i < n : 
        return i
    else:
        return -1