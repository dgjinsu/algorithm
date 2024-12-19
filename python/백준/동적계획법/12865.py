import sys
input = sys.stdin.readline

n, k = map(int, input().split())

things = [[0, 0] for _ in range(n + 1)]
dp = [[0] * (k + 1) for i in range(n + 1)]

for i in range(1, n + 1):
  a, b = map(int, input().split())
  things[i] = [a,b]

for i in range(1, n + 1):
  w, v = things[i][0], things[i][1]
  for j in range(1, k + 1):
    if w > j:
      dp[i][j] = dp[i-1][j]
    else:
      dp[i][j] = max(dp[i-1][j-w] + v, dp[i-1][j])

print(dp[-1][-1])  