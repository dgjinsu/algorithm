import sys
input = sys.stdin.readline

c = int(input())
num = list(map(int, input().split()))

min_num, max_num = min(num), max(num)

print(min_num * max_num)