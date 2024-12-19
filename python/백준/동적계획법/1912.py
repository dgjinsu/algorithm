import sys
input = sys.stdin.readline

n = int(input())
numbers = list(map(int, input().split()))

dp = [0] * n
dp[0] = numbers[0]
for i in range(1, n):
  now = numbers[i]

  if dp[i-1] + now < now:
    dp[i] = now
  elif dp[i-1] + now > 0:
    dp[i] = dp[i-1] + now
  else:
    dp[i] = now

print(max(dp))

