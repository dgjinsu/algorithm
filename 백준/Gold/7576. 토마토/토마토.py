import sys
from collections import deque
input = sys.stdin.readline

m, n = map(int, input().split())
arr = []
visit = [[0] * m for _ in range(n)]

q = deque()
for i in range(n):
    arr.append(list(map(int, input().split())))
    for j in range(len(arr[i])):
        if arr[i][j] == 1:
            q.append((i, j))
            visit[i][j] = 1
        elif arr[i][j] == -1:
            visit[i][j] = -1

dx = [1, -1, 0, 0]
dy = [0, 0, -1, 1]

max_days = -1
def bfs():
    global max_days
    while q:
        x, y = q.popleft()
        if visit[x][y] > max_days:
            max_days = visit[x][y]
        for i in range(4):
            nx, ny = x + dx[i], y + dy[i]
            if nx >= 0 and ny >= 0 and nx < n and ny < m:
                if arr[nx][ny] == 0 and visit[nx][ny] == 0:
                    visit[nx][ny] = visit[x][y] + 1
                    q.append((nx, ny))
bfs()
flag = True
for i in range(n):
    for j in range(m):
        if visit[i][j] == 0:
            print(-1)
            flag = False
            break
    if not flag:
        break
if flag:
    print(max_days - 1)