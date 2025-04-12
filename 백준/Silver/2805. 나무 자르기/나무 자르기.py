import sys
input = sys.stdin.readline

tree_cnt, target = map(int, input().split())

trees = list(map(int, input().split()))
results = []

left, right = 0, 10**9

while left <= right:
    mid = (left + right) // 2

    cut_tree = 0
    for tree in trees:
        if mid < tree:
            cut_tree += (tree - mid)
    
    if cut_tree == target:
        results.append(mid)
        break
    elif cut_tree > target:
        results.append(mid)
        left = mid +1
    elif cut_tree < target:
        right = mid - 1

print(max(results))