import sys
from itertools import combinations
input = sys.stdin.readline

n, m = map(int, input().split())

city = []
for i in range(n):
  city.append(list(map(int, input().split())))

chickens = []
homes = []

for i in range(n):
  for j in range(n):
    if city[i][j] == 1:
      homes.append((i, j))
    if city[i][j] == 2:
      chickens.append((i, j))

result = []
for choiced_chickens in combinations(chickens, m):
  dis = []
  for home in homes:
    chicken_dis = []
    x2, y2 = home
    for chicken in choiced_chickens:
      x1, y1 = chicken
      chicken_dis.append(abs(x2 - x1) + abs(y2 - y1))
    dis.append(min(chicken_dis))
  result.append(sum(dis))
print(min(result))
