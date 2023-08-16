import sys

n, c = map(int, sys.stdin.readline().split())

house = []
for _ in range(n):
    house.append(int(sys.stdin.readline()))

house.sort()

left, right = 0, max(house) - min(house)
while left <= right:
    set_count = 1
    mid = (left + right) // 2
    before, after = house[0], house[1]
    for i in range(1, len(house) - 1):
        if after - before >= mid:
            set_count += 1
            before = house[i]
            after = house[i+1]
        else:
            after = house[i+1]
    if after - before >= mid:
        set_count += 1

    if set_count >= c:
        left = mid + 1
    else:
        right = mid - 1


print(right)