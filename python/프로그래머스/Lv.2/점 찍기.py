def solution(k, d):
    answer = 0
    for i in range(0, d//k + 1):
        x = i * k
        y = (d ** 2 - x ** 2) ** 0.5
        x_cnt = y // k
        # print(f'x 좌표가 {x}일 때 갯수: {x_cnt+1}')
        answer += (x_cnt + 1)
        
    return answer