import sys
input = sys.stdin.readline

n, m = map(int, input().split())

map = {}
for _ in range(n):
  tmp = input().rstrip()
  map[tmp] = 1

cnt = 0
for _ in range(m):
  tmp = input().rstrip()
  if tmp in map:
    cnt += 1

print(cnt)
