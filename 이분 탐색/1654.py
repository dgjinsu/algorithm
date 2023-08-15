import sys

n, k = map(int, sys.stdin.readline().split())
wire = []
for _ in range(n):
    wire.append(int(sys.stdin.readline()))

left, right = 1, max(wire)
while left <= right:
    wire_count = 0
    mid = (left + right) // 2
    for i in wire:
        wire_count += (i // mid)
    if wire_count == k:
        left = mid + 1
    if wire_count < k:
        right = mid - 1
    elif wire_count > k:
        left = mid + 1

print(right)

