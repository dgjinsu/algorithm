import sys
input = sys.stdin.readline

s = input().rstrip()
set_s = set()

for i in range(len(s)):
  for j in range(i + 1, len(s) + 1):
    set_s.add(s[i:j])

print(len(set_s))