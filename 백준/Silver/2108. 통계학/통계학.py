import sys
input = sys.stdin.readline

n = int(input())
nums = []
for _ in range(n):
    nums.append(int(input()))

cnt = [0] * 8001

print(round(sum(nums) / n))
nums.sort()
print(nums[len(nums) // 2])

for i in nums:
    if i < 0:
        cnt[4000 + abs(i)] += 1
    else:
        cnt[i] += 1

results = []
max_cnt = max(cnt)
for i in range(len(cnt)):
    if cnt[i] == max_cnt:
        if i > 4000:
            results.append(-1 * (i - 4000))
        else:
            results.append(i)
if len(results) > 1:
    results.sort()
    print(results[1])
else:
    print(results[0])
print(nums[-1] - nums[0])