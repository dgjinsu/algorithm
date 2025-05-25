from collections import deque

def solution(storage, requests):
    # 하나만 요청이 들어오면 접근 가능한 컨테이너
    # 두번 반복된 요청이 들어오면 크레인으로 모든 컨테이너를 꺼냄

    storage_list = [[0] * len(storage[0]) for _ in range(len(storage))]
    
    for i in range(len(storage_list)):
        for j in range(len(storage_list[0])):
            storage_list[i][j] = storage[i][j]
            
    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]

    def bfs(a, b):
        visit = [[0] * len(storage[0]) for _ in range(len(storage))]
        visit[a][b] = 1
        q = deque()
        q.append((a, b))
        while q:
            x, y = q.popleft()
            if x == 0 or y == 0 or x == len(storage) -1 or y == len(storage[0]) - 1:
                return True
            for i in range(4):
                nx, ny = x + dx[i], y + dy[i]
                if 0 <= nx < len(storage) and 0 <= ny < len(storage[0]):
                    if visit[nx][ny] == 0 and storage_list[nx][ny] == "-1":
                        visit[nx][ny] = 1
                        q.append((nx, ny))
        
        return False
    
    def poll_all_container(target):
        for i in range(len(storage_list)):
            for j in range(len(storage_list[0])):
                if storage_list[i][j] == target:
                    storage_list[i][j] = "-1"
                    
    def poll_outline_container(target):
        tmp = [[0] * len(storage_list[0]) for _ in range(len(storage_list))]
        for i in range(len(storage_list)):
            for j in range(len(storage_list[0])):
                # print(f'{i}, {j} 좌표이며 {storage_list[i][j]} 의 bfs 결과는: {bfs(i, j)}')
                if storage_list[i][j] == target and bfs(i, j):
                    tmp[i][j] = "-1"
        for i in range(len(tmp)):
            for j in range(len(tmp[0])):
                if tmp[i][j] == "-1":
                    storage_list[i][j] = "-1"
    
    for request in requests:
        isCrain = len(request) == 2
        
        if isCrain:
            # 전체 컨테이너 제거
            poll_all_container(request[0])
        else:
            # 접근 가능한 컨테이너만 제거
            poll_outline_container(request)
        
        # print(f'현재 명령어: {request}')
        # for i in storage_list:
        #     print(i)
    
    cnt = 0
    for i in storage_list:
        for j in i:
            if j != "-1":
                cnt += 1
    return cnt