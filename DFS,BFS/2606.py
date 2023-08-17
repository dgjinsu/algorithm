import sys
from collections import deque

com = int(sys.stdin.readline())
line = int(sys.stdin.readline())
graph = [[] for _ in range(com + 1)]
visited = [0] * (com + 1)
for _ in range(line):
    a, b = map(int, sys.stdin.readline().split())
    graph[a].append(b)
    graph[b].append(a)

cnt = 0
def bfs(a):
    q = deque([1])
    visited[1] = 1
    global cnt

    while q:
        v = q.popleft()
        for i in graph[v]:
            if visited[i] == 0:
                visited[i] = 1
                cnt += 1
                q.append(i)
bfs(1)
print(cnt)