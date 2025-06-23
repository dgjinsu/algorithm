import sys
from collections import deque
input = sys.stdin.readline

# 잔을 선택 -> 다마심, 마신 후 원래 위치로 놓기
# 연속 3잔은 X

# 가장 많은 포도주를 마시게

n = int(input())
drinks = [0] * 10001
for i in range(n):
    drinks[i] = int(input())
dp = [0] * 10001

dp[0] = drinks[0]
dp[1] = dp[0] + drinks[1]
dp[2] = max(drinks[0] + drinks[2], drinks[1] + drinks[2], dp[1])
for i in range(3, n):
    dp[i] = max(dp[i-2] + drinks[i], dp[i-3] + drinks[i-1] + drinks[i], dp[i-1])

print(max(dp))