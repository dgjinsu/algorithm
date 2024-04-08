def solution(name, yearning, photo):
    answer = []
    d = dict()
    # 이름: 그리움 dict
    for i in range(len(name)):
        d[name[i]] = yearning[i]
    
    for p in photo:
        s = 0
        for n in p:
            if n in d:
                s += d[n]
        answer.append(s)

    return answer