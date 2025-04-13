import sys
input = sys.stdin.readline

n = int(input())
k = int(input())

left, right = 1, k
result = 0

def findForwardCnt(mid):
    tmp=0
    a = min(n, mid)
    for i in range(1, a + 1):
        tmp += min(mid//i, n)
    return tmp

while(left <= right):
    mid = (left + right) // 2
    cnt = findForwardCnt(mid)

    if cnt < k:
        left = mid + 1
    else:
        right = mid - 1
        result = mid
print(result)