def solution(edges):
    # 정점 조건: 나가는 수 2이상, 들어오는 수 0
    # 막대 그래프 수: 나가는 수 0, 들어오는 수 1인 정점의 개수
    # 8자 그래프 수: 나가는 수 2, 들어오는 수 2인 정점의 개수
    # 도넛 그래프 수: 나머지 수
    
    l = [[0,0] for _ in range(1000000)] # 0: 나가는 것, 1: 들어오는 것
    
    for i in edges:
        s = i[0]
        e = i[1]
        l[s][0] += 1
        l[e][1] += 1
    
    answer = [0, 0, 0, 0]
    m = -1
    for index, i in enumerate(l):
        # 정점
        if i[0] > m and i[1] == 0:
            m = i[0]
            answer[0] = index
            
    for i in edges:
        # 정점에서 나간 간선을 받은 노드는 들어온 간선 수 -1
        if i[0] == answer[0]:
            if l[i[1]][1] == 1:
                continue
            l[i[1]][1] -= 1
    
    for index, i in enumerate(l):
        # 막대
        if i[0] == 0 and i[1] == 1:
            answer[2] += 1
        # 8자
        if i[0] == 2 and i[1] == 2:
            answer[3] += 1
    answer[1] = l[answer[0]][0] - answer[2] - answer[3]
    # 정점, 도넛, 막대, 8자
    return answer