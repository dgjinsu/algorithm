import sys
from collections import deque
input = sys.stdin.readline

n, m = map(int, input().split()) #사다리, 뱀
ladder = {}
snake = {}
graph = [0] * 101
visited = [False] * 101
for _ in range(n):
    a, b = map(int, input().split())
    ladder[a] = b
for _ in range(m):
    a, b = map(int, input().split())
    snake[a] = b

def bfs():
    q = deque()
    q.append(1)
    while q:
        x = q.popleft()
        if x == 100:
            print(graph[x])
            break
        for i in range(1, 7):
            nx = x + i
            if 1 <= nx < 101:
                if nx in ladder:
                    nx = ladder[nx]
                if nx in snake:
                    nx = snake[nx]
                if not visited[nx]:
                    q.append(nx)
                    visited[nx] = True
                    graph[nx] = graph[x] + 1
bfs()
