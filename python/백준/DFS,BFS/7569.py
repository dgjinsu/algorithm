import sys
from collections import deque
input = sys.stdin.readline

m, n, h = map(int, input().split()) #열 행 높이
graph = []
q = deque()
for i in range(h):
    tmp = []
    for j in range(n):
        tmp.append(list(map(int, input().split())))
        for k in range(m):
            if tmp[j][k] == 1:
                q.append([i, j, k]) #익은 토마토 q에 저장
    graph.append(tmp)
dx = [1, -1, 0, 0, 0, 0]
dy = [0, 0, 1, -1, 0, 0]
dz = [0, 0, 0, 0, 1, -1]

def bfs():
    while q:
        x, y, z = q.popleft()
        for i in range(6):
            nx = x + dx[i]
            ny = y + dy[i]
            nz = z + dz[i]
            if 0 <= nx < h and 0 <= ny < n and 0 <= nz < m:
                if graph[nx][ny][nz] == 0:
                    graph[nx][ny][nz] = graph[x][y][z] + 1
                    q.append([nx, ny, nz])
bfs()
answer = -1
for i in graph:
    for j in i:
        for k in j:
            if k==0:
                print(-1)
                exit(0)
        answer = max(answer, max(j))

print(answer - 1)