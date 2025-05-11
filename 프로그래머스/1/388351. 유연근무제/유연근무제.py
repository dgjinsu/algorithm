def solution(schedules, timelogs, startday):
    answer = 0
    for i in range(len(schedules)):
        now_days = startday - 1
        flag = True
        for j in range(7):
            if now_days != 5 and now_days != 6: # 평일
                a = (schedules[i] // 100 * 60) + schedules[i] % 100
                b = (timelogs[i][j] // 100 * 60) + timelogs[i][j] % 100
                if b - a > 10: # 지각
                    flag = False
            now_days = (now_days + 1) % 7
        if flag:
            answer += 1
        
    return answer