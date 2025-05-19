import sys
from collections import deque
input = sys.stdin.readline

n, m = map(int, input().split())

arr = [[0] * m for _ in range(n)]
visit = [[0] * m for _ in range(n)]
for i in range(n):
    t = input().strip()
    for j in range(m):
        arr[i][j] = int(t[j])

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]
def bfs(a, b):
    global n, m
    visit[a][b] = 1
    q = deque()
    q.append((a, b))
    while q:
        x, y = q.popleft()
        if x == n-1 and y == m-1:
            print(visit[x][y])
            break
        for i in range(4):
            nx, ny = x + dx[i], y + dy[i]
            if nx >= 0 and ny >= 0 and nx < n and ny < m:
                if arr[nx][ny] == 1 and visit[nx][ny] == 0:
                    visit[nx][ny] = visit[x][y] + 1
                    q.append((nx, ny))

bfs(0, 0)