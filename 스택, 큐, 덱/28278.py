import sys

list = []

n = int(sys.stdin.readline())

for _ in range(n):
    command = sys.stdin.readline().split()
    if command[0] == "1":
        list.append(command[1])
    if command[0] == "2":
        if list:
            print(list.pop())
        else:
            print(-1)
    if command[0] == "3":
        print(len(list))
    if command[0] == "4":
        if list:
            print(0)
        else:
            print(1)
    if command[0] == "5":
        if list:
            print(list[-1])
        else:
            print(-1)
