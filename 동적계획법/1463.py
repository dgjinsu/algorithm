import sys
input = sys.stdin.readline
n = int(input())
dp = [0] * 1000001
dp[1] ,dp[2], dp[3] = 0, 1, 1
for i in range(4, len(dp)):
  tmp = []
  if i % 3 == 0:
    tmp.append(dp[i//3] + 1)
  if i % 2 == 0:
    tmp.append(dp[i//2] + 1)
  tmp.append(dp[i-1] + 1)

  dp[i] = min(tmp)
  
  if i == n:
    break

print(dp[n])