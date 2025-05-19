import sys
from collections import deque
input = sys.stdin.readline

t = int(input())

for _ in range(t):
    # 문서 개수, 타겟 문서
    n, m = map(int, input().split())
    idx = m
    q = deque(list(map(int, input().split())))
    cnt = 1

    while True:
        isBiggest = True
        for i in range(0, len(q)):
            if q[0] < q[i]:
                isBiggest = False
        
        if isBiggest:
            if idx == 0:
                print(cnt)
                break
            cnt += 1
            q.popleft()
            idx -= 1
            if idx < 0:
                idx = len(q) - 1
        # 더 큰게 있을 때
        else:
            q.append(q.popleft())
            idx -= 1
            if idx < 0:
                idx = len(q) - 1