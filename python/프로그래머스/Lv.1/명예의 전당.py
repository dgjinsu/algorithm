import heapq
def solution(k, score):
    q = []
    answer = []

    def updateq(s):
        if len(q) < k:
            heapq.heappush(q, s)
            answer.append(q[0])
            return
        if s > q[0]:
            if len(q) >= k:
                tmp = heapq.heappop(q)
            heapq.heappush(q, s)
        answer.append(q[0])
        
        
    for s in score:
        updateq(s)
    
    return answer