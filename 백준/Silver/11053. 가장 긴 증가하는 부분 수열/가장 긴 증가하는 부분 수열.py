import sys
input = sys.stdin.readline

n = int(input())

nums = list(map(int, input().split()))
dp = [1] * n
for i in range(n):
    max_dp = 0
    for j in range(i):
        # print(f'현재 값: {nums[i]}, 비교 값: {nums[j]}')
        if nums[i] > nums[j] and max_dp < dp[j]:
            max_dp = dp[j]
    dp[i] = max(dp[i], max_dp + 1)

print(max(dp))