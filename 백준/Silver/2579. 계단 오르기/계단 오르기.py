import sys
input = sys.stdin.readline

n = int(input())

s = [0] * 301
for i in range(n):
  s[i] = int(input())

dp = [0] * 301

dp[0], dp[1] = s[0], s[0] + s[1]
dp[2] = max(s[0] + s[2], s[1] + s[2])

for i in range(3, n):
  # print(f'{i}번째 계단에서 {dp[i-3] + s[i-1] + s[i]}, {dp[i-2] + s[i]} 중 택1')
  dp[i] = max(dp[i-3] + s[i-1] + s[i], dp[i-2] + s[i])

print(dp[n-1])