import sys
from collections import deque
input = sys.stdin.readline
dx = [2, 2, -2, -2, 1, 1, -1, -1]
dy = [1, -1, 1, -1, 2, -2, 2, -2]
t = int(input())
for _ in range(t):
    n = int(input())
    a1, b1 = map(int, input().split())
    a2, b2 = map(int, input().split())
    graph = [[] * n for __ in range(n)]
    visited = [[0] * n for __ in range(n)]

    cnt = 1
    def bfs(a, b):
        global a2, b2
        q = deque()
        q.append([a,b])
        global cnt
        visited[a][b] = cnt
        while q:
            x, y = q.popleft()
            if x == a2 and y == b2:
                print(visited[x][y] - 1)
                break
            for i in range(8):
                nx = x + dx[i]
                ny = y + dy[i]
                if 0 <= nx < len(graph) and 0 <= ny < len(graph):
                    if visited[nx][ny] == 0:
                        q.append([nx, ny])
                        visited[nx][ny] = visited[x][y] + 1
    bfs(a1, b1)
