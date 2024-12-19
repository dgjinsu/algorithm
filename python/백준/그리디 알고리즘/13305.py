import sys
input = sys.stdin.readline

n = int(input())
dis = list(map(int, input().split()))
cost = list(map(int, input().split()))
min_cost = cost[0]
answer = 0
for i in range(0, len(dis)):
  if cost[i] < min_cost:
    min_cost = cost[i]
  answer += dis[i] * min_cost 

print(answer)