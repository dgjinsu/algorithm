def solution(targets):
    n = len(targets)
    targets.sort(key = lambda x: [x[1], x[0]])
    
    answer = 0
    e = 0
    for i in range(n):
        if targets[i][0] >= e:
            answer += 1
            e = targets[i][1]
    return answer
