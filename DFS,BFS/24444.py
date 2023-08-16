import sys
from collections import deque


n, m, r = map(int, sys.stdin.readline().split())
graph = [[] for _ in range(n+1)]
visited = [0] * (n+1)
for _ in range(m):
    a, b = map(int, sys.stdin.readline().split())
    graph[a].append(b)
    graph[b].append(a)
for i in graph:
    i.sort()

cnt = 1
def bfs(v):
    global cnt
    q = deque([r])
    visited[r] = 1
    while q:
        a = q.popleft()
        for i in graph[a]:
            if visited[i] == 0:
                cnt += 1
                visited[i] = cnt
                q.append(i)

bfs(r)
for i in range(1, n+1):
    print(visited[i])