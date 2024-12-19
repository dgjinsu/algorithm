import sys
import heapq as hq
input = sys.stdin.readline
n, e = map(int, input().split())
INF = int(10e9)
graph = [[] for _ in range(n + 1)]
for _ in range(e):
  a, b, c = map(int, input().split())
  graph[a].append((b, c))
  graph[b].append((a, c))

v1, v2 = map(int, input().split())

q = []
def dijkstra(start):
  dis = [INF] * (n + 1)
  dis[start] = 0
  hq.heappush(q, (0, start))
  while q:
    dist, now_node = hq.heappop(q)
    for n_n, weight in graph[now_node]:
      cost = dist + weight #n_n노드까지 오는데 걸린 가중치 + 다음으로 가는 가중치
      if cost < dis[n_n]:
        dis[n_n] = cost
        hq.heappush(q, (cost, n_n))
  return dis
dis_first = dijkstra(1)
dis_v1 = dijkstra(v1)
dis_v2 = dijkstra(v2)

v1_first_dis = dis_first[v1] + dis_v1[v2] + dis_v2[n]
v2_first_dis = dis_first[v2] + dis_v2[v1] + dis_v1[n]

result = min(v1_first_dis, v2_first_dis)
if result < INF:
  print(result)
else:
  print(-1)