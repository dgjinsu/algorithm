from collections import deque
import sys
input = sys.stdin.readline

test_case = int(input())

dx = [1, 1, -1, -1, 2, 2, -2, -2]
dy = [2, -2, 2, -2, 1, -1, 1, -1]

board = []
x, y, tx, ty, size = 0, 0, 0, 0, 0

def bfs():
    q = deque([[x, y]])
    while(q):
        tmp = q.popleft()
        a, b = tmp[0], tmp[1]
        if a == tx and b == ty:
            return board[a][b]
        for i in range(8):
            nx = a + dx[i]
            ny = b + dy[i]
            if nx >= 0 and ny >= 0 and nx < size and ny < size:
                if board[nx][ny] == 0:
                    board[nx][ny] = board[a][b] + 1
                    q.append([nx, ny])

for _ in range(test_case):
    size = int(input())
    x, y = map(int, input().split())
    tx, ty = map(int, input().split())

    board = [[0] * size for _ in range(size)]

    print(bfs())