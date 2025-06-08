import sys
from collections import deque
input = sys.stdin.readline

n = int(input())

homes = []
visit = [[0] * n for _ in range(n)]

for i in range(n):
    t = list(map(int, list(input().strip())))
    homes.append(t)

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]
cnt = 0
def dfs(x, y):
    global cnt, n
    visit[x][y] = 1
    cnt += 1

    for i in range(4):
        nx, ny = x + dx[i], y + dy[i]
        if 0 <= nx < n and 0 <= ny < n:
            if homes[nx][ny] == 1 and visit[nx][ny] == 0:
                dfs(nx, ny)
    return cnt

result = []
for i in range(n):
    for j in range(n):
        if homes[i][j] == 1 and visit[i][j] == 0:
            result.append(dfs(i, j))
            cnt = 0

result.sort()
print(len(result))
for r in result:
    print(r)