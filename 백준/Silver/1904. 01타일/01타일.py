import sys
input = sys.stdin.readline

# N = 1 (1) => 1
# N = 2 (11 00) => 2
# N = 3 (111 100 001) => 3
# N = 4 (1111 0000 0011 1001 1100) => 5
# N = 5 (11111 00111 10011 11001 11100 10000 00100 00001) => 8

# f(n) = f(n-1) + f(n-2)

n = int(input())
dp = [0] * 1000001
dp[1], dp[2] = 1, 2
for i in range(3, n + 1):
    dp[i] = (dp[i-1] + dp[i-2]) % 15746

print(dp[n])