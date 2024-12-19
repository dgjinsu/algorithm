from collections import deque
def solution(sequence, k):
    answer = [0, 0]
    
    rs = reversed(sequence)
    q = deque()
    s = 0
    start, end = 0, len(sequence) - 1
    q_size = len(sequence) + 1
    for idx, num in enumerate(rs):
        q.append(num)
        start = len(sequence) - 1 - idx
        
        s += num
        if s > k:
            tmp = q.popleft()
            s -= tmp
            end -= 1
        if s == k and q_size >= len(q):
            q_size = len(q)
            answer[0] = start
            answer[1] = end
    return answer
