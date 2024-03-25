import sys

while True:
    sentence = sys.stdin.readline().rstrip()
    if sentence == ".":
        break

    stack = []
    check = True
    for i in sentence:
        if i == "(":
            stack.append(i)
        if i == ")":
            if len(stack) != 0 and stack[-1] == "(":
                stack.pop()
            else:
                print("no")
                check = False
                break

        if i == "[":
            stack.append(i)
        if i == "]":
            if len(stack) != 0 and stack[-1] == "[":
                stack.pop()
            else:
                print("no")
                check = False
                break
    if len(stack) == 0 and check:
        print("yes")
    elif check:
        print("no")
