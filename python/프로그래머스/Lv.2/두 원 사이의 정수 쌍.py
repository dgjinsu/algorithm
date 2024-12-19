import math
def solution(r1, r2):
    answer = 0
    # y^2 = r^2 - x^2
    for i in range(1, r2 + 1):
        cnt_r2 = int(((r2*r2) - (i*i))**0.5)
        if i < r1:
            cnt_r1 = math.ceil(((r1*r1) - (i*i))**0.5)
            answer += (cnt_r2 - cnt_r1) + 1
        else:
            answer += cnt_r2 + 1
    return answer * 4