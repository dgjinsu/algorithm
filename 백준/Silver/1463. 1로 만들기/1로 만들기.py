import sys
input = sys.stdin.readline

n = int(input())
dp = [0] * (10 ** 6 + 1)

dp[1], dp[2], dp[3] = 0, 1, 1
for i in range(4, n + 1):
  re = []
  if i % 3 == 0:
    re.append(dp[i // 3] + 1)
  if i % 2 == 0:
    re.append(dp[i // 2] + 1)
  re.append(dp[i-1] + 1)
  dp[i] = min(re)
  # print(f'${i} 숫자는 후보가 {re} 이다. ')

print(dp[n])