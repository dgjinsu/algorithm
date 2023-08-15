import sys

n = int(sys.stdin.readline())

for _ in range(n):
    input = sys.stdin.readline()
    stack = []
    answer = "YES"
    for i in input:
        if i == "(":
            stack.append(i)
        if i == ")":
            if len(stack) == 0:
                answer = "NO"
                break
            else:
                stack.pop()

    if len(stack) != 0:
        answer = "NO"
    print(answer)
