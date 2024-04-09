def solution(park, routes):
    # 넘어가거나 장애물이 있으면 무시
    answer = []
    now_loc = [0, 0]
    for idx1, i in enumerate(park):
        for idx2, j in enumerate(i):
            if j == 'S':
                now_loc[0], now_loc[1] = idx1, idx2
                
                
    for order in routes:
        tmp1, tmp2 = order.split(" ")
        d, jump = tmp1, int(tmp2)
        next_loc = now_loc.copy()
        flag = True
        
        if d == "N":
            for i in range(jump):
                next_loc[0] -= 1
                if next_loc[0] < 0 or park[next_loc[0]][next_loc[1]] == "X":
                    flag = False
                    break
        if d == "S":
            for i in range(jump):
                next_loc[0] += 1
                if next_loc[0] > len(park) - 1 or park[next_loc[0]][next_loc[1]] == "X":
                    flag = False
                    break
        if d == "W":
            for i in range(jump):
                next_loc[1] -= 1
                if next_loc[1] < 0 or park[next_loc[0]][next_loc[1]] == "X":
                    flag = False
                    break
        if d == "E":
            for i in range(jump):
                next_loc[1] += 1
                if next_loc[1] > len(park[0]) - 1 or park[next_loc[0]][next_loc[1]] == "X":
                    flag = False
                    break
        if flag:
            now_loc = next_loc.copy()
        
    return now_loc