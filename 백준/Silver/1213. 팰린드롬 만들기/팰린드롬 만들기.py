import sys
input = sys.stdin.readline

arr = [0] * 26

name = input().strip()
for i in name:
  arr[ord(i) - 65] += 1

cnt = 0
one_cnt_idx = -1
for i in range(26):
  if arr[i] % 2 != 0:
    cnt += 1
    one_cnt_idx = i
if cnt > 1:
  print("I'm Sorry Hansoo")
  exit()

# 하나인 문자 처리
arr[one_cnt_idx] -= 1

result = []
for i in range(26):
  for j in range(0, arr[i], 2):
    result.append(chr(i + 65))

re_result = []
for i in range(len(result) -1 , -1, -1):
  re_result.append(result[i])

if cnt == 1:
  result.extend([chr(one_cnt_idx + 65)])
result.extend(re_result)

for i in result:
  print(i, end="")