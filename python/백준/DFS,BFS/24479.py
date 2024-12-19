import sys
sys.setrecursionlimit(10**9)        # recur 횟수

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
def dfs(graph, a, visited):
    global cnt
    visited[a] = cnt
    for i in graph[a]:
        if visited[i] == 0:
            cnt += 1
            dfs(graph, i, visited)


dfs(graph, r, visited)
for i in range(1, n+1):
    print(visited[i])