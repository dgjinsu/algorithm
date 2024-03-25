import sys
from collections import deque
input = sys.stdin.readline

n, m = map(int, input().split())

graph = [list(map(int, input().rstrip())) for _ in range(n)]
visited = [[0] * m for _ in range(n)]
dx = [1,-1,0,0]
dy = [0,0,1,-1]

def bfs(a, b):
    q = deque()
    q.append([a,b])
    visited[a][b] = 1
    while q:
        x, y = q.popleft()
        if x == n - 1 and y == m - 1:
            print(visited[x][y])
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < n and 0 <= ny < m:
                if visited[nx][ny] == 0 and graph[nx][ny] == 1:
                    q.append([nx, ny])
                    visited[nx][ny] = visited[x][y] + 1
bfs(0, 0)
