def getPartialMatch(N):
    m = len(N)
    pi = [0] * m
    # KMP로 N에서 N을 찾는다 (begin은 1부터)
    begin = 1
    matched = 0
    # 비교할 문자가 N의 끝에 도달할 때까지 부분 일치를 모두 기록
    while begin + matched < m:
        if N[begin + matched] == N[matched]:
            matched += 1
            pi[begin + matched - 1] = matched
        else:
            if matched == 0:
                begin += 1
            else:
                begin += matched - pi[matched - 1]
                matched = pi[matched - 1]
    return pi

