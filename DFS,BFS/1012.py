import sys
from collections import deque
input = sys.stdin.readline

t = int(input())
dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]
answer = []
for i in range(t):
    m, n, k = map(int, input().split())
    graph = [[0] * n for _ in range(m)]
    visited = [[0] * n for _ in range(m)]

    for _ in range(k):
        a, b = map(int, input().split())
        graph[a][b] = 1
    
    def bfs(a, b):
        q = deque()
        q.append([a,b])
        visited[a][b] = 1
        while q:
            x, y = q.popleft()
            for i in range(4):
                nx = x + dx[i]
                ny = y + dy[i]
                if 0 <= nx < len(graph) and 0 <= ny < len(graph[0]):
                    if visited[nx][ny] == 0 and graph[nx][ny] == 1:
                        visited[nx][ny] = 1
                        q.append([nx, ny])
    cnt = 0
    for a in range(m):
        for b in range(n):
            if graph[a][b] == 1 and visited[a][b] == 0:
                bfs(a,b)
                cnt += 1
    answer.append(cnt)

for i in answer:
    print(i)