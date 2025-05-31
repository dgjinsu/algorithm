import sys
input = sys.stdin.readline

# 0 1 2 3 4 5 6 7 8 9 
# 0 1 2 3 4 5 6 7 8 9 
# 0 1 2 3 4 5 6 7 8 9 
# 0 1 2 3 4 5 6 7 8 9 

n = int(input())

dp = [[1 for _ in range(10)] for _ in range(n)]
dp[0][0]= 0 

for i in range(1, n):
  for j in range(0, 10):
    if j == 0:
      dp[i][j] = dp[i-1][1] % 10**9
    elif j == 9:
      dp[i][j] = dp[i-1][8] % 10**9
    else:
      dp[i][j] = dp[i-1][j-1] % 10**9 + dp[i-1][j+1] % 10**9

print(sum(dp[-1]) % 10**9)