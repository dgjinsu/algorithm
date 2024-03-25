import sys
input = sys.stdin.readline

n, k = map(int, input().split())
money = []
for _ in range(n):
  money.append(int(input()))
money.reverse()
answer = 0 
while k > 0:
  for i in money:
    if k // i > 0:
      answer += k // i
      k %= i

print(answer)