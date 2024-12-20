import sys
input = sys.stdin.readline

n = int(input())
scores = list(map(int, input().split()))
max_score = max(scores)

for i in range(len(scores)):
  scores[i] = scores[i] / max_score * 100

print(sum(scores) / n)