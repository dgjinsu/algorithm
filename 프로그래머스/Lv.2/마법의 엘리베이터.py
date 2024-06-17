def solution(storey):
    answer = 0
    while storey:
        num = storey % 10
        flag = False
        if num == 5:
            tmp = storey // 10
            if tmp % 10 >= 5:
                answer += (10 - num)
                flag = True
            else: 
                answer += num
        if num > 5:
            answer += (10 - num)
            flag = True
        if num < 5:
            answer += num
        
        storey //= 10
        if flag:
            storey += 1
    return answer
        
        