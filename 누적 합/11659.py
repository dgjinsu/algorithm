import sys
from collections import deque
input = sys.stdin.readline

n, m = map(int, input().split())

num = list(map(int, input().split()))
num_sum = [0] * (len(num) + 1)

sum = 0
for idx, i in enumerate(num):
    sum += i
    num_sum[idx + 1] = sum

print(num_sum)
for _ in range(m):
    a, b = map(int, input().split())
    print(num_sum[b] - num_sum[a - 1])