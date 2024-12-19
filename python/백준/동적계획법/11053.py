import sys
input = sys.stdin.readline

n = int(input())
dp = [0] * n
numbers = list(map(int, input().split()))

for i in range(n):
  tmp = 0
  for j in range(i):
    if numbers[i] > numbers[j]:
      if tmp < dp[j]:
        tmp = dp[j]
  dp[i] = tmp + 1

print(max(dp))