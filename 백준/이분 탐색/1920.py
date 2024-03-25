import sys
from collections import deque

n = int(sys.stdin.readline())
num = sys.stdin.readline().split()

m = sys.stdin.readline()
find = sys.stdin.readline().split()

set_num = set(num)
for i in find:
    if i in set_num:
        print(1)
    else:
        print(0)

# n = int(sys.stdin.readline())
# num = sys.stdin.readline().split()

# m = sys.stdin.readline()
# find = sys.stdin.readline().split()
# num.sort()

# for i in find:
#     left, right = 0, n - 1
#     isExist = False

#     while left <= right:
#         mid = (left + right) // 2
#         if i == num[mid]:
#             isExist = True
#             print(1)
#             break
#         if i > num[mid]:
#             left = mid + 1
#         if i < num[mid]:
#             right = mid - 1
    
#     if not isExist:
#         print(0)