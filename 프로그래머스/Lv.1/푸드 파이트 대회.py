def solution(food):
    left_person = ""
    for idx, i in enumerate(food):
        tmp = str(idx) * (i//2)
        left_person += tmp
    
    right_person = ""
    for i in range(len(left_person) - 1, -1, -1):
        right_person += left_person[i]
        
    return left_person + "0" + right_person