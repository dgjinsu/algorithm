import sys
import heapq as hq
from collections import deque
input = sys.stdin.readline

heap = []
n = int(input())
for _ in range(n):
    x = int(input())
    if x:
        hq.heappush(heap, -x)
    if x == 0:
        if heap:
            print(-hq.heappop(heap))
        else:
            print(0)