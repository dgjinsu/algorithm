import sys
input = sys.stdin.readline

n, m = map(int, input().split())

arr = []
for i in range(n):
  arr.append(input().rstrip())

answer = []
def sol(check, a, b):
  ch = check #W
  tmpW, tmpB = 0, 0
  for i in range(8):
    for j in range(8):
      if (i + j) % 2 == 0:
        if arr[a + i][b + j] != "W":
          tmpW += 1
        else:
          tmpB += 1
      else:
        if arr[a + i][b + j] != "B":
          tmpW += 1
        else:
          tmpB += 1
  return min(tmpW, tmpB)

for i in range(n - 7):
  for j in range(m - 7):
    first = arr[i][j] #first = W
    answer.append(sol(first, i, j))

print(min(answer))