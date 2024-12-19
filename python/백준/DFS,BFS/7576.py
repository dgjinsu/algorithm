import sys
from collections import deque
input = sys.stdin.readline

n, m = map(int, input().split())

graph = [list(map(int, input().split())) for _ in range(m)]
visited = [[-1] * n for _ in range(m)]
check = False
q = deque()
for i in range(m):
    for j in range(n):
        if graph[i][j] == 1:
            q.append([i, j])
            visited[i][j] = 0
        if graph[i][j] == -1:
            visited[i][j] = 0
        if graph[i][j] == 0:
            check = True
if not check:
    print(0)
    exit()

dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]
def bfs():
    while q:
        x, y = q.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < m and 0 <= ny < n:
                if visited[nx][ny] == -1 and graph[nx][ny] == 0:
                    q.append([nx, ny])
                    visited[nx][ny] = visited[x][y] + 1
bfs()

answer = -1

for i in visited:
    for j in i:
        if j == -1:
            print(-1)
            exit()
    answer = max(answer, max(i))
print(answer)