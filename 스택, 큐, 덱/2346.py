import sys
from collections import deque

n = int(sys.stdin.readline())

b = deque(enumerate(map(int, sys.stdin.readline().split()), start=1))
answer = []
for _ in range(n):
    idx, num = b.popleft()
    answer.append(str(idx))
    if len(b) == 0:
        break

    if num > 0:
        b.rotate(-(num - 1))
    if num < 0:
        b.rotate(-num)

print(" ".join(answer))
