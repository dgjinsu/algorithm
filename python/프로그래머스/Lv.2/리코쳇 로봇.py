from collections import deque
def solution(board):
    dx = [1, -1, 0, 0]
    dy = [0, 0, -1, 1]
    visited = [[0] * len(board[0]) for _ in range(len(board))]
    
    def bfs(a, b):
        result = 1
        q = deque()
        q.append([a,b])
        visited[a][b] = 1
        while q:
            x, y = q.popleft()
            if board[x][y] == "G":
                return visited[x][y]
            for i in range(4):
                nx, ny = x, y # 초기화
                # 장애물을 만날때까지
                while True:
                    nx, ny = nx + dx[i], ny + dy[i]
                    if nx >= 0 and ny >= 0 and nx < len(board) and ny < len(board[0]):
                        if board[nx][ny] == "D": # 멈춰섬
                            nx, ny = nx - dx[i], ny - dy[i]
                            
                            if visited[nx][ny] == 0:
                                q.append([nx, ny])
                                visited[nx][ny] = visited[x][y] + 1
                            break
                    else:
                        nx, ny = nx - dx[i], ny - dy[i] # 넘어갔으니 원복
                        if visited[nx][ny] == 0:
                            q.append([nx, ny])
                            visited[nx][ny] = visited[x][y] + 1
                        break
        return -1
    
    s_x, s_y = 0, 0
    for i in range(len(board)):
        for j in range(len(board[i])):
            if board[i][j] == "R":
                s_x, s_y = i, j
    
    answer = bfs(s_x, s_y)
    if answer > 0:
        answer -= 1
    return answer