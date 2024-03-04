import sys
intput = sys.stdin.readline

def w(a, b, c):
  if a <= 0 or b <= 0 or c <= 0:
    return 1
  if a > 20 or b > 20 > c > 20:
    return w(20, 20, 20)
  if a < b and b < c:
    return w(a, b, c-1) + w(a, b-1, c-1) - w(a, b-1, c)
  return w(a-1, b, c) + w(a-1, b-1, c) + w(a-1, b, c-1) - w(a-1, b-1, c-1)

dp = [[[0] * 21 for _ in range (21)] for _ in range (21)]
print(dp)
# while True:
#   a, b, c = input().split()
#   if a == 1 and b == 1 and c == 1:
#     break