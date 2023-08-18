import sys
from collections import deque
input = sys.stdin.readline

n, k = map(int, input().split())
graph = [] * 100001
visited = [0] * 100001
cnt = 1
dx = [-1, 1, 2]
def bfs(a):
    global cnt
    q = deque()
    q.append(a)
    visited[a] = cnt
    while q:
        x = q.popleft()
        if x == k:
            print(visited[x] - 1)
        for i in range(3):
            if i == 2:
                nx = x * dx[i]
            else: 
                nx = x + dx[i]
            if 0 <= nx <= 100000:
                if visited[nx] == 0:
                    q.append(nx)
                    visited[nx] = visited[x] + 1
bfs(n)