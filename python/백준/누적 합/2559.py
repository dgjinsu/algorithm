import sys
input = sys.stdin.readline

n, k = map(int, input().split())
num = list(map(int, input().split()))
num_sum = []
num_sum.append(0)

sum = 0
for i in num:
  sum += i
  num_sum.append(sum)

answer = []
for i in range(1, n - k + 2):
  tmp = num_sum[i + k - 1] - num_sum[i - 1]
  answer.append(tmp)

print(max(answer))