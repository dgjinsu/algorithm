def solution(friends, gifts):
    num = len(friends)
    trade = [[0] * num for _ in range(num)]
    times = [0] * num # 지수를 나타냄
    result = [0] * num
    pti = {}
    for i in range(num):
        pti[friends[i]] = i
    
    for i in gifts:
        s, r = map(str, i.split())
        trade[pti[s]][pti[r]] += 1
        times[pti[s]] += 1
        times[pti[r]] -= 1
    
    
    for i in range(num):
        for j in range(num):
            if i == j:
                continue
            if trade[i][j] > trade[j][i]: # 준거 > 받은거
                result[i] += 1 # 받을거 추가
            if trade[i][j] == trade[j][i]: # 주고 받지 않거나 같을 때
                if times[i] > times[j]:
                    result[i] += 1 # 받을거 추가

                    
    print(result)
    return max(result)