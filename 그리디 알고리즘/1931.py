import sys
input = sys.stdin.readline

n = int(input())

room = []
for _ in range(n):
  a, b = map(int, input().split())
  room.append((b, a))

room.sort()

finish = 0
answer = 0
for i in room:
  if i[1] >= finish:
    answer += 1
    finish = i[0]

print(answer)