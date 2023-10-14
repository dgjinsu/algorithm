import sys
intput = sys.stdin.readline
# 파이썬은 시간초과가 난다. c++로는 가능

# cnt1 = cnt2 = 0
# def fib(n):
#   global cnt1
#   if n == 1 or n == 2:
#     return 1
#   else:
#     return (fib(n-1) + fib(n-2))

def fib_dp(n):
  dp = [0] * n
  dp[0], dp[1] = 1, 1
  for i in range(2, n):
    dp[i] = dp[i-1] + dp[i-2]
  return dp[n-1]

n = int(input())

answer = fib_dp(n)

print(f'{answer} {n-2}')