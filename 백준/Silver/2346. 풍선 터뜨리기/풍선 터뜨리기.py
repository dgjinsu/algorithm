import sys
from collections import deque
input = sys.stdin.readline

n = int(input())
balloons = list(map(int, input().split()))

d = deque()
for idx, i in enumerate(balloons):
    d.append([i, idx + 1])

result = []

while True:
    tmp = d.popleft()
    result.append(tmp[1])
    if len(d) == 0:
        break
    if tmp[0] > 0:
        for i in range(tmp[0] - 1):
            d.append(d.popleft())
    else:
        for i in range(abs(tmp[0])):
            d.appendleft((d.pop()))
for i in result:
    print(i, end=" ")