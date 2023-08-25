import sys
from collections import deque
input = sys.stdin.readline

n = int(input())
k = int(input())

left = 1
right = n * n
while left <= right:
    tmp = 0
    mid = (left + right) // 2
    for i in range(1, n + 1):
        tmp += min(n, mid // i)
    if tmp >= k:
        answer = mid
        right = mid - 1
    else:
        left = mid + 1
print(answer)