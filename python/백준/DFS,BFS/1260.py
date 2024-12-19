import sys
from collections import deque

n, m, v = map(int, sys.stdin.readline().split())
graph = [[] for _ in range(n + 1)]
visited = [0] * (n + 1)
visited1 = [0] * (n + 1)
answer1 = []
answer2 = []
for _ in range(m):
    a, b = map(int, sys.stdin.readline().split())
    graph[a].append(b)
    graph[b].append(a)
for i in graph:
    i.sort()
def bfs(a):
    q = deque([a])
    visited[a] = 1
    answer1.append(a)
    while q:
        v = q.popleft()
        for i in graph[v]:
            if visited[i] == 0:
                visited[i] = 1
                answer1.append(i)
                q.append(i)

def dfs(graph, visited, a):
    visited[a] = 1
    answer2.append(a)
    for i in graph[a]:
        if visited[i] == 0:
            dfs(graph, visited, i)

bfs(v)
dfs(graph, visited1, v)

print(" ".join(map(str, answer2)))
print(" ".join(map(str, answer1)))