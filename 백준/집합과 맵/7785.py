import sys
input = sys.stdin.readline

n = int(input())
m = {}
for _ in range(n):
  name, type = map(str, input().split())
  if type == "enter":
    m[name] = 1
  else:
    del m[name]
answer = sorted(m.keys(), reverse=True)

print("\n".join(answer))