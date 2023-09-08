import sys
from collections import deque
import heapq as hq
input = sys.stdin.readline

n, k = map(int , input().split())

# 2부터 해야 0초를 먼저 이동할 수 있고
# 1 보다 -1이 먼저여야 n, k = 4, 6 같은 예제를 통과할 수 있음
# 혹은 방문 체크를 deque 에서 뺄 때 체크하면 통과
dx = [2, -1, 1] 
graph = [-1] * 100001 # 0 ~ 100,000
def bfs():
  graph[n] = 0
  q = deque([n])
  while q:
    x = q.popleft()
    if x == k:
      print(graph[x])
      exit()
    for i in range(3):
      if dx[i] == 2:
        nx = x * 2
        if nx >= 0 and nx < 100001:
          if graph[nx] == -1: # 방문 x
            graph[nx] = graph[x] # 순간이동
            q.appendleft(nx)
      else:
        nx = x + dx[i]
        if nx >= 0 and nx < 100001:
          if graph[nx] == -1:
            graph[nx] = graph[x] + 1
            q.append(nx)

bfs()