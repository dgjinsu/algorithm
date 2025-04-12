import sys
input = sys.stdin.readline

home_cnt, wifi_cnt = map(int, input().split())
homes = [int(input()) for _ in range(home_cnt)]

homes.sort()
left, right = 1, homes[-1] - homes[0]
result = 0  

def setup(mid):
    prev = homes[0]
    count = 1
    for i in range(1, home_cnt):
        if homes[i] - prev >= mid:
            count += 1
            prev = homes[i]
    return count

while left <= right:
    mid = (left + right) // 2
    count = setup(mid)

    if count < wifi_cnt:
        right = mid - 1
    else:
        result = mid
        left = mid + 1

print(result)
