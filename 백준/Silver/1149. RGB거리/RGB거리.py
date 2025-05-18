import sys
input = sys.stdin.readline

n = int(input())
dp = [[0 for _ in range(3)] for _ in range(1000)]
dp[0][0], dp[0][1], dp[0][2] = map(int, input().split())

for i in range(1, n):
    r, g, b = map(int, input().split())

    # R
    dp[i][0] = min(dp[i-1][1], dp[i-1][2]) + r
    # G
    dp[i][1] = min(dp[i-1][0], dp[i-1][2]) + g
    # B
    dp[i][2] = min(dp[i-1][0], dp[i-1][1]) + b

print(min(dp[n-1]))