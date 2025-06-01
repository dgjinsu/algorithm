import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline

n, m, r = map(int, input().split())

g = [[] for _ in range(n + 1)]

for _ in range(m):
    a, b = map(int, input().split())
    g[a].append(b)
    g[b].append(a)

for i in g:
    i.sort()

visit = [0] * (n + 1)
cnt = 1

def dfs(start):
    global cnt
    visit[start] = cnt
    for next in g[start]:
        if visit[next] == 0:
            cnt += 1
            dfs(next)

dfs(r)

for i in range(1, n + 1):
    print(visit[i])
