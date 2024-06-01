from collections import deque
dx = [1, -1, 0, 0]
dy = [0, 0, -1, 1]

def findPoint(maps, target):
    for i in range(len(maps)):
        for j in range(len(maps[i])):
            if maps[i][j] == target:
                return (i, j)
            
def bfs(maps, visit, a, b, t_x, t_y):
    q = deque()
    q.append([a,b])
    while(q):
        x, y = q.popleft()
        if x == t_x and y == t_y:
            return visit[x][y]
        for i in range(4):
            nx, ny = x + dx[i], y + dy[i]
            if nx >= 0 and ny >= 0 and nx < len(maps) and ny < len(maps[0]):
                if visit[nx][ny] == 0 and (maps[nx][ny] != "X"):
                    visit[nx][ny] = visit[x][y] + 1
                    q.append([nx, ny])
    return -1
    
def solution(maps):
    answer = 0
    visit = [[0] * 101 for _ in range(101)]
    l_x, l_y = findPoint(maps, "L")
    s_x, s_y = findPoint(maps, "S")
    e_x, e_y = findPoint(maps, "E")
    
    tmp1 = bfs(maps, visit, s_x, s_y, l_x, l_y) # 레버까지 거리
    visit = [[0] * 101 for _ in range(101)]
    tmp2 = bfs(maps, visit, l_x, l_y, e_x, e_y) # 출구까지 거리
    
    if tmp1 == -1 or tmp2 == -1:
        return -1
    else:
        return tmp1 + tmp2
