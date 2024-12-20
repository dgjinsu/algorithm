n, m = map(int, input().split(" "))

arr = [i for i in range(n+1)]

for _ in range(m):
  start, end = map(int, input().split())
  arr[start:end+1] = arr[start:end+1][::-1]

print(*arr[1:])