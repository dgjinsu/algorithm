import sys
input = sys.stdin.readline

n = int(input())
dancing = set(["ChongChong"])

for _ in range(n):
    a, b = input().strip().split()
    if a in dancing or b in dancing:
        dancing.add(a)
        dancing.add(b)

print(len(dancing))