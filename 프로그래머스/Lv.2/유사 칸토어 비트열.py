def f(n, r):
    if n == 1:
        if r <= 2:
            return r
        else:
            return r - 1
    div = 5 ** (n-1)
    area = r // div
    cnt_1 = 4 ** (n-1)
    
    if r % div == 0:
        area -= 1
    
    if area < 2:
        return cnt_1 * area + f(n-1, r - div * area)
    if area > 2:
        return cnt_1 * (area - 1) + f(n-1, r - div * area)
    else:
        return cnt_1 * 2


def solution(n, l, r):
    answer = f(n,r) - f(n, l-1)
    return answer