import sys
input = sys.stdin.readline

n = int(input())
dp = [0] * 10000
drinks = [0] * 10000
for i in range(n):
  drinks[i] = int(input())

dp[0] = drinks[0]
dp[1] = drinks[0] + drinks[1]
dp[2] = max(drinks[0] + drinks[2], drinks[1] + drinks[2], dp[1])

for i in range(3, n):
  a = dp[i-3] + drinks[i-1] + drinks[i] # 연속 2잔 
  b = dp[i-2] + drinks[i] # 연속 1잔
  c = dp[i-1] # 안 마심
  dp[i] = max(a,b,c)

print(max(dp))