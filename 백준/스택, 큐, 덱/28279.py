import sys
from collections import deque

n = int(sys.stdin.readline())
deque = deque()
for _ in range(n):
    command = sys.stdin.readline().split()
    if command[0] == "1":
        deque.appendleft(command[1])
    if command[0] == "2":
        deque.append(command[1])
    if command[0] == "3":
        if deque:
            print(deque.popleft())
        else:
            print(-1)
    if command[0] == "4":
        if deque:
            print(deque.pop())
        else:
            print(-1)
    if command[0] == "5":
        print(len(deque))
    if command[0] == "6":
        if deque:
            print(0)
        else:
            print(1)
    if command[0] == "7":
        if deque:
            print(deque[0])
        else:
            print(-1)
    if command[0] == "8":
        if deque:
            print(deque[-1])
        else:
            print(-1)
