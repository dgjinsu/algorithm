from collections import deque
def solution(cards1, cards2, goal):
    answer = ''
    idx1 = 0
    idx2 = 0
    idx_goal = 0
    while idx_goal < len(goal):
        if idx1 < len(cards1) and cards1[idx1] == goal[idx_goal]:
            idx1 += 1
            idx_goal += 1
            continue
        
        if idx2 < len(cards2) and cards2[idx2] == goal[idx_goal]:
            idx2 += 1
            idx_goal += 1
            continue
            
        return "No"
        
    return "Yes"