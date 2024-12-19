import sys
input = sys.stdin.readline

sen = input().rstrip().split("-")
for i in range(len(sen)):
  tmp = sen[i].split("+")
  partition = 0
  for j in tmp:
    partition += int(j) # 00009 같은 수는 int 로 감싸주면 9가 된다
  sen[i] = str(partition)

answer = "-".join(sen)
print(eval(answer))
