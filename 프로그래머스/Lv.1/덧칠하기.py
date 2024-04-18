def solution(n, m, section):
    answer = 0
    paint_end = 0
    for s in section:
        if s <= paint_end:
            continue
        paint_end = s + m - 1 # 페인트 칠
        answer+= 1
        
    return answer