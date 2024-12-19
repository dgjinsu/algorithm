import sys
from collections import deque

n, k = map(int, sys.stdin.readline().split())

print(n)
print(k)

person = deque(range(1, n + 1))
answer = []
while True:
    if len(person) == 0:
        break
    for _ in range(k - 1):
        person.append(person.popleft())
    answer.append(str(person.popleft()))

print("<" + ", ".join(answer) + ">")
