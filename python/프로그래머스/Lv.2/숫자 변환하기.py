from collections import deque
def solution(x, y, n):
    answer = 0
    numbers = [0] * 1000001
    dx = [2, 3]
    dx.append(n)
    
    def bfs(start):
        q = deque()
        q.append(start)
        while q:
            x = q.popleft()
            if x == y:
                return numbers[y]
            for i in range(3):
                nx = x * dx[i]
                if i == 2:
                    nx = x + dx[i]
                if nx <= 1000000 and numbers[nx] == 0:
                    numbers[nx] = numbers[x] + 1
                    q.append(nx)
        return -1
    return bfs(x)