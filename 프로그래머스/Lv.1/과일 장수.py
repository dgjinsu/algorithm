def solution(k, m, score):
    # 사과의 최대 점수 k
    # 한 상자의 사과 개수 m
    # 사과들 점수 score
    answer = 0
    
    score.sort(reverse=True)
    for i in range(0, len(score)):
        if (i+1) % m == 0:
            answer += (score[i] * m)
    
    return answer