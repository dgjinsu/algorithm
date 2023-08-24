import sys
import heapq as hq
from collections import deque
input = sys.stdin.readline

heap = []
n = int(input())
for _ in range(n):
    x = int(input())
    if x != 0:
        hq.heappush(heap, (abs(x), x)) # 절대값, 원래값 을 넣어 튜플 비교
    else:
        if heap:
            print(f'정답 {hq.heappop(heap)[1]}')
        else:
            print("정답: 0")