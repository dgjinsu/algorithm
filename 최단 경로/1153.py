import sys
import heapq as hq
input = sys.stdin.readline

v, e = map(int, input().split())
k = int(input())
INF = int(10e9)
dis = [INF] * (v + 1)
graph = [[] for _ in range(v + 1)]

for i in range(e):
  u, v, w = map(int, input().split())
  graph[u].append((v,w))

q = []
def dijkstra(start):
  dis[start] = 0
  hq.heappush(q, (0, start))
  while q:
    dist, now_node = hq.heappop(q)
    for n_n, weight in graph[now_node]:
      cost = dist + weight #n_n노드까지 오는데 걸린 가중치 + 다음으로 가는 가중치
      if cost < dis[n_n]:
        dis[n_n] = cost
        hq.heappush(q, (cost, n_n))
dijkstra(k)

for i in dis[1:]:
  if i != INF:
    print(i)
  else:
    print("INF")