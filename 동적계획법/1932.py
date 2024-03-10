import sys
input = sys.stdin.readline

n = int(input())

dp = [[] for _ in range(n)]
dp[0] = list(map(int, input().split()))
for i in range(1, n):
  numbers = list(map(int, input().split()))
  for j in range(len(numbers)):
    if j == 0:
      numbers[j] = dp[i-1][j] + numbers[j]
      continue
    if j == len(numbers) - 1:
      numbers[j] = dp[i-1][j-1] + numbers[j]
      continue
    numbers[j] = max(dp[i-1][j-1] + numbers[j], dp[i-1][j] + numbers[j])
  dp[i] = numbers

print(max(dp[n-1]))
