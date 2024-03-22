import sys
input = sys.stdin.readline

n = int(input())

numbers = list(map(int, input().split()))

dp1 = [1] * n
dp2 = [1] * n
dp1[0], dp2[n-1] = 1, 1

for i in range(1, n):
  tmp = 1
  for j in range(i):
    if numbers[i] > numbers[j]:
      if dp1[j] + 1 > tmp:
        tmp = dp1[j] + 1
  dp1[i] = tmp

for i in range(n-2, -1, -1):
  tmp = 1
  for j in range(n-1, i, -1):
    if numbers[i] > numbers[j]:
      if dp2[j] + 1 > tmp:
        tmp = dp2[j] + 1
  dp2[i] = tmp

answer = 0
for i in range(n):
  tmp = dp1[i] + dp2[i]
  if tmp > answer:
    answer = tmp

print(answer - 1)