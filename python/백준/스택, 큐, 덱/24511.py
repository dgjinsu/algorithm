import sys
from collections import deque

n = int(sys.stdin.readline())
q_d = sys.stdin.readline().split()
q_d_number = sys.stdin.readline().split()
queue = deque()

for idx, i in enumerate(q_d):
    if i == "0":
        queue.append(q_d_number[idx])

k = int(sys.stdin.readline())
num = sys.stdin.readline().split()
answer = []

if queue:
    for i in num:
        answer.append(str(queue.pop()))
        queue.appendleft(i)

    print(" ".join(answer))
else:
    print(" ".join(num))
