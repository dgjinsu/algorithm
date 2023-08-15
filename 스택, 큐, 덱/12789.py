import sys
from collections import deque

n = int(sys.stdin.readline())
person = deque(map(int, sys.stdin.readline().split()))
stack = []
index = 1
while True:
    if stack and stack[-1] == index:
        stack.pop()
        index = index + 1
        continue

    if (len(stack) > 0 and len(person) == 0) or (len(stack) == 0 and len(person) == 0):
        break

    tmp = person.popleft()
    if tmp == index:
        index = index + 1
        continue

    stack.append(tmp)

if stack:
    print("Sad")
else:
    print("Nice")
