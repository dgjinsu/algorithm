def solution(k, tangerine):
    answer = 0
    m = dict()
    for t in tangerine:
        if t in m:
            m[t] += 1
        else:
            m[t] = 1
    tmp = list(m.values())
    tmp.sort(reverse = True)
    for i in tmp:
        k -= i
        answer += 1
        if k <= 0:
            break
    
    return answer