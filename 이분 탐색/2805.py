import sys

n, m = map(int, sys.stdin.readline().split())

tree = list(map(int, sys.stdin.readline().split()))

left, right = int(1), int(max(tree))
while left <= right:
    mid = (left + right) // 2
    get_tree = 0
    for i in tree:
        if i > mid:
            get_tree += (i - mid)
    if get_tree >= m:
        left = mid + 1
    else:
        right = mid - 1

print(right)