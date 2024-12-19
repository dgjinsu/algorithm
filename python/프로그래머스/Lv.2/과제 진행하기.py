from collections import deque
class Homework:
    def __init__(self, name, s, play_time):
        self.name = name
        self.s = s
        self.play_time = play_time
    def __str__(self):
        return f'{self.name}, {self.s}, {self.play_time}'
    
def solution(plans):
    # 0: 과제명
    # 1: 시작
    # 2: 종료
    answer = []
    result = []
    homework_list = []
    for i in plans:
        s_hour, s_minute = map(int, i[1].split(":"))
        s_time = s_hour*60 + s_minute
        homework_list.append(Homework(i[0], s_time, int(i[2])))
        
    # 시작 시간으로 정렬
    homework_list.sort(key = lambda x : x.s)
    homework_deque = deque(homework_list)
    
    index = 0
    stop_list = [] # 멈춘 과제 stack
    now = homework_deque.popleft() # 현재 과제
    time = now.s # 시간 시작
    while (True):
        if len(homework_deque) == 0 and len(stop_list) == 0 and now == None:
            break
            
        # 과제 하나 끝
        if now != None and now.play_time == 0:
            result.append(now)
            now = None


        if len(homework_deque) != 0:
            if homework_deque and time == homework_deque[0].s: # 다음 시작이 오면
                stop_list.append(now) # stop list 추가
                now = homework_deque.popleft() # 현재 과제 변경
        
        # 과제가 끝났고 새로 시작할게 없다면
        if now == None:
            if len(stop_list) != 0:
                now = stop_list.pop()
                
        time += 1 # 시간 증가
        if now != None:
            now.play_time -= 1 # 과제 시간 감소

    for i in result:

        answer.append(i.name)
    return answer