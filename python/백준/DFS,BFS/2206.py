import sys
from collections import deque
input = sys.stdin.readline

n, m = map(int, input().split())
graph = [list(map(int, input().rstrip())) for _ in range(n)]
visited = [[[0] * 2 for _ in range(m)] for _ in range(n)] #높이 열 행

dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]
def bfs(a, b, c):
    q = deque()
    q.append([a, b, c])
    visited[a][b][c] = 1
    while q:
        x, y, z = q.popleft()
        if x == n - 1 and y == m - 1:
            print(visited[x][y][z])
            exit()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < n and 0 <= ny < m:
                if graph[nx][ny] == 1 and z == 0: #벽을 부순적이 없을 때
                    visited[nx][ny][1] = visited[x][y][z] + 1 #벽을 부숨
                    q.append([nx, ny, 1])
                if graph[nx][ny] == 0 and visited[nx][ny][z] == 0: #다음이 벽이 아닐 때
                    visited[nx][ny][z] = visited[x][y][z] + 1
                    q.append([nx, ny, z])

bfs(0, 0, 0)
print(-1)