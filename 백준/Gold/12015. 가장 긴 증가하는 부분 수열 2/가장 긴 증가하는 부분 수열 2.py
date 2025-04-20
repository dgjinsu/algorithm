import sys
input = sys.stdin.readline

a = int(input())
nums = list(map(int, input().split()))

arr = [nums[0]]
max_len = 1

def binary_search(num):
    left, right = 0, len(arr)-1
    while left <= right:
        mid = (left + right) // 2
        if arr[mid] >= nums[i]:
            right = mid - 1
        else:
            left = mid + 1
    return left

for i in range(1, a):
    if arr[-1] < nums[i]:
        arr.append(nums[i])
        max_len = len(arr)
    elif arr[-1] > nums[i]:
        # 자기 자리 찾아 그 자리에 값 덮어씌우기
        find_idx = binary_search(nums[i])
        arr[find_idx] = nums[i]
        # max_len 최신화
        max_len = max(max_len, find_idx + 1)

print(max_len)