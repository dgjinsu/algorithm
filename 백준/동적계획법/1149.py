import sys
input = sys.stdin.readline

n = int(input())
dp = [[] for _ in range(n)]

r, g, b = map(int, input().split())
dp[0] = [r, g, b]

for i in range(1, n):
  r, g, b = map(int, input().split())
  r_ = min(dp[i-1][1] + r, dp[i-1][2] + r)
  g_ = min(dp[i-1][0] + g, dp[i-1][2] + g)
  b_ = min(dp[i-1][0] + b, dp[i-1][1] + b)
  dp[i] = [r_, g_, b_]

print(min(dp[n-1]))
