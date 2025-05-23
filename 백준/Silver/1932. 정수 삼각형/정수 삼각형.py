import sys
input = sys.stdin.readline

n = int(input())
arr =[]
for i in range(n):
    arr.append(list(map(int, input().split())))

dp = [[0] * n for _ in range(n)]
dp[0][0] = arr[0][0]

for i in range(1, n):
    for j in range(i + 1):
        if j == 0:
            dp[i][j] = arr[i][j] + dp[i-1][j]
        elif j == i:
            dp[i][j] = arr[i][j] + dp[i-1][j-1]
        else:
            dp[i][j] = arr[i][j] + max(dp[i-1][j-1], dp[i-1][j])

print(max(dp[-1]))

# 7
# 3 8
# 8 1 0
# 2 7 4 4
# 4 5 2 6 5

# j 가 0이면 dp[i-1][j]
# j 가 i면 dp[i-1][j-1]
# dp[i][j] = dp[i-1][j-1], dp[i-1][j]