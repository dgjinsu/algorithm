import sys
input = sys.stdin.readline

t = int(input())

dp = [0] * 100
dp[0], dp[1], dp[2], dp[3] = 1, 1, 1, 2

for i in range(3, len(dp)):
    dp[i] = dp[i - 2] + dp[i - 3]

for _ in range(t):
    n = int(input())
    print(dp[n - 1])