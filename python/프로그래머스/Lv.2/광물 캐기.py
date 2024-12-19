from collections import deque
class M:
    def __init__(self, d, i, s):
        self.d = d
        self.i = i
        self.s = s
    def __str__(self):
        return f'd: {self.d}, i: {self.i}, s: {self.s}'
    
    
def solution(picks, minerals):
    answer = 0
    
    use_picks_num = len(minerals) // 5 # 사용해야하는 곡괭이 수
    if len(minerals) % 5 != 0:
        use_picks_num += 1
    
    range_sum = []
    for _ in range(use_picks_num):
        range_sum.append(M(0,0,0))

    
    for i in range(0, len(minerals)):
        if minerals[i] == "diamond":
            range_sum[i//5].d += 1
        if minerals[i] == "iron":
            range_sum[i//5].i += 1
        if minerals[i] == "stone":
            range_sum[i//5].s += 1
            
    # 곡괭이 수가 광물의 집합 보다 작은 경우
    if sum(picks) < len(range_sum):
        range_sum = range_sum[:sum(picks)]
    
    range_sum.sort(key = lambda x: (-x.d, -x.i, -x.s))
    q = deque()
    
    for i in range_sum:
        if picks[0] > 0: # 다이아
            answer += (i.d + i.i + i.s)
            picks[0] -= 1
        elif picks[1] > 0: # 철
            answer += (5*i.d + i.i + i.s)
            picks[1] -= 1
        elif picks[2] > 0: # 돌
            answer += (25*i.d + 5*i.i + i.s)
            picks[2] -= 1
            
    return answer