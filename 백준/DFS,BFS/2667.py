import sys
from collections import deque
input = sys.stdin.readline

n = int(sys.stdin.readline())
graph = [list(map(int, input().rstrip())) for _ in range(n)]
visited = [[0] * n for _ in range(n)]
dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]
answer = []

def bfs(a, b):
    visited[a][b] = 1
    cnt = 1
    q = deque()
    q.append([a, b])
    while q:
        x, y = q.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if nx >= 0 and ny >= 0 and nx < len(graph) and ny < len(graph):
                if visited[nx][ny] == 0 and graph[nx][ny] == 1:
                    cnt += 1
                    visited[nx][ny] = 1
                    q.append([nx, ny])
    answer.append(cnt)


for i in range(n):
    for j in range(n):
        if graph[i][j] == 1 and visited[i][j] == 0:
            bfs(i, j)
            
answer.sort()
print(len(answer))
for i in answer:
    print(i)