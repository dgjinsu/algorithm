import sys
input = sys.stdin.readline

n = int(input())

dp = [0] * 1000001
dp[1], dp[2] = 1, 2
for i in range(3, n+1):
  dp[i] = dp[i-1] + dp[i-2]

print(dp[n])


# n = 1   1
# n = 2   2
# n = 3   001 100 111   3
# n = 4   5
# n = 5   00001 00100 00111 10000 10011 11001 11100 11111   8
# n = 6   000000 000011 001001 001100 001111 100001 100100 110000 110011 111001 111100 111111 12