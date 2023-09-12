import sys
input = sys.stdin.readline

n, m = map(int, input().split())
d = {}
r_d = {}
for i in range(1, n + 1):
  name = input().rstrip()
  d[str(i)] = name
  r_d[name] = i
for i in range(m):
  command = input().rstrip()
  if command in d:
    print(d[command])
  else:
    print(r_d[command])