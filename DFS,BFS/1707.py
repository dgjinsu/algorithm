import sys
from collections import deque
input = sys.stdin.readline

t = int(input())
for _ in range(t):
    v, e = map(int, input().split())
    graph = [[] for _ in range(v + 1)]
    visited = [0] * (v + 1)
    for __ in range(e):
        a, b = map(int, input().split())
        graph[a].append(b)
        graph[b].append(a)

    def bfs(a, color):
        q = deque()
        q.append(a)
        visited[a] = color
        while q:
            x = q.popleft()
            for i in graph[x]:
                if visited[i] == 0:
                    visited[i] = -1 * visited[x]
                    q.append(i)
                if visited[i] != 0 and visited[i] == visited[x]: # 탐색중인 노드와 색이 같다면 FALSE
                    return False
        return True
    for i in range(1, v + 1):
        if visited[i] == 0:
            result = bfs(i, 1)
            if not result:
                break
    if result:
        print("YES")
    else:
        print("NO")
