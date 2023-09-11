import sys
import heapq as hq
input = sys.stdin.readline
INF = int(1e9)
def dijkstra(start):
  q = []
  dis = [INF] * (n + 1)
  dis[start] = 0
  hq.heappush(q, (0, start))
  while q:
    dist, now_node = hq.heappop(q)
    if dis[now_node] < dist:
      continue
    for n_n, weight in graph[now_node]:
      cost = dist + weight
      if dis[n_n] > cost:
        dis[n_n] = cost
        hq.heappush(q, (cost, n_n))
  return dis

test_case = int(input())
for _ in range(test_case):
  n, m, t = map(int, input().split()) #n:교차로 수 | m:도로 수 | t:목적지 후보 수
  s, g, h = map(int, input().split()) #s: 출발지 | g, h: 반드시 지나야하는 도로

  graph = [[] for _ in range(n + 1)]
  goal = []

  for _ in range(m): #도로 입력
    a, b, d = map(int, input().split())
    graph[a].append((b, d))
    graph[b].append((a, d))
  
  for _ in range(t):
    tmp = int(input())
    goal.append(tmp)

  first_dij = dijkstra(s)
  require_g = dijkstra(g)
  require_h = dijkstra(h)

  answer = []
  for i in goal:
    if first_dij[g] + require_g[h] + require_h[i] == first_dij[i] or first_dij[h] + require_h[g] + require_g[i] == first_dij[i]:
      answer.append(i)
  answer.sort()
  print(" ".join(map(str, answer)))