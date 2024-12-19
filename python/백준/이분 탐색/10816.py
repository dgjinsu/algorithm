import sys

n = sys.stdin.readline()
num = sys.stdin.readline().split()

m = sys.stdin.readline()
find = sys.stdin.readline().split()

d = {}
for i in num:
    if i in d:
        d[i] = d[i] + 1
    else:
        d[i] = 1

answer = []
for i in find:
    if i in d:
        answer.append(str(d[i]))
    else: 
        answer.append(str(0))
    
print(" ".join(answer))