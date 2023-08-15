import sys

n = int(sys.stdin.readline())
list = []
for _ in range(n):
    number = int(sys.stdin.readline())
    if number == 0:
        list.pop()
        continue

    list.append(number)

print(sum(list))
