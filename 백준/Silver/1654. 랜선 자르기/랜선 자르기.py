import sys
input = sys.stdin.readline

n, k = map(int, input().split())

lens = [int(input()) for _ in range(n)]
results = []

left, right = 0, 2**31 - 1

while left <= right:
    mid = (left + right) // 2
    
    cnt = sum([len // mid for len in lens])

    if cnt < k:
        right = mid - 1
    elif cnt > k:
        left = mid + 1
        results.append(mid)
    elif cnt == k:
        left = mid + 1
        results.append(mid)

print(max(results))