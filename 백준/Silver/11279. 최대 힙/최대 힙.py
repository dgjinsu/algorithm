import sys
import heapq
input = sys.stdin.readline

n = int(input())

h = []
result = []
for _ in range(n):
    c = int(input())
    if c == 0:
        if len(h):
            result.append(heapq.heappop(h))
        else:
            result.append(0)
    else:
        heapq.heappush(h, -c)

for i in result:
    print(-i)