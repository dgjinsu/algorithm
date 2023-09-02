import sys
input = sys.stdin.readline

sen = input().rstrip()
arr = [[0 for _ in range(26)] for _ in range(len(sen))]
arr[0][ord(sen[0]) - 97] = 1
for i in range(1, len(sen)):
  tmp = ord(sen[i]) - 97 
  for j in range(26):
    if j == tmp:
      arr[i][j] = arr[i - 1][j] + 1
    else:
      arr[i][j] = arr[i - 1][j]
q = int(input())
for _ in range(q):
  find, start, end = map(str, input().split())
  start, end = int(start), int(end)
  if start == 0:
    print(arr[end][ord(find) - 97])
    continue
  print(arr[end][ord(find) - 97] - arr[start - 1][ord(find) - 97])
