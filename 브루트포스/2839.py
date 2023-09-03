import sys
input = sys.stdin.readline
n = int(input())

answer = []
for i in range(0, (n//5) + 1):  
  tmp = n
  if n // 5 > 0:  
    tmp = n - (5 * i)
  cnt = tmp // 3
  if tmp % 3 == 0:
    answer.append(i + cnt)

if len(answer) != 0:
  print(min(answer))
else:
  print(-1)