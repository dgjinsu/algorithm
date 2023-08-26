import sys
from collections import deque
from bisect import bisect_left

input = sys.stdin.readline

n = int(input())

a = list(map(int, input().split()))

lis = []
lis.append(a[0])
# for i in a:
#     left, right = 0, len(lis) - 1
#     if lis[-1] < i:
#         lis.append(i)
#         continue
#     while left <= right:
#         mid = (left + right) // 2
#         if lis[mid] >= i:
#             right = mid - 1
#         if lis[mid] < i:
#             left = mid + 1
#     lis[left] = i

# print(len(lis))

# bisect 사용
for i in a:
    if lis[-1] < i:
        lis.append(i)
        continue
    index = bisect_left(lis, i)
    lis[index] = i
print(len(lis))