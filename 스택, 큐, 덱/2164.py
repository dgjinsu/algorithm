import sys
from collections import deque

n = int(sys.stdin.readline())
queue = deque(range(1, n + 1))

if n == 1:
    print(1)
else:
    while True:
        queue.popleft()
        if len(queue) == 1:
            break
        queue.append(queue.popleft())
    print(queue.pop())
