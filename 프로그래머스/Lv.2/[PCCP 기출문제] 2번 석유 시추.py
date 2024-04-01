from collections import deque

def solution(land):
    l1 = len(land) # 세로
    l2 = len(land[0]) # 가로
    dx = [1, -1, 0, 0]
    dy = [0, 0, 1, -1]
    
    visit = [[0] * l2 for _ in range(l1)] # 방문 여부
    result = [0] * l2
    def bfs(a, b):
        cnt = 1
        visit[a][b] = 1
        q = deque()
        q.append((a,b))
        find_col = {b} # bfs를 돌며 석유가 포함된 열을 보관할 set
        while(q):
            x, y = q.popleft()
            for i in range(4):
                n_x = x + dx[i]
                n_y = y + dy[i]
                if n_x >= 0 and n_y >= 0 and n_x < l1 and n_y < l2:
                    if visit[n_x][n_y] == 0 and land[n_x][n_y] == 1:
                        q.append((n_x, n_y))
                        visit[n_x][n_y] = 1
                        find_col.add(n_y)
                        cnt += 1
        # 각 열을 돌면서 석유량추가
        for f in find_col:
            result[f] += cnt
            
    for i in range(l2): # 8
        cnt = 0
        for j in range(l1): # 5
            if visit[j][i] == 0 and land[j][i] == 1:
                bfs(j, i)
        result.append(cnt)
    return max(result)