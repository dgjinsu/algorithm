def solution(today, terms, privacies):
    def change_days(target):
        s_target = target.split(".")
        return 28 * 12 * (int(s_target[0]) % 2000) + 28 * int(s_target[1]) + int(s_target[2])
    
    
    answer = []
    d = {}
    now = change_days(today)
    for i in terms:
        tmp = i.split()
        d[tmp[0]] = int(tmp[1]) * 28
        
    print(d)
    for idx, i in enumerate(privacies):
        tmp = i.split(" ")
        start = change_days(tmp[0])
        plus = d[tmp[1]]
        print(f'start + plus 값: {int(start) + int(plus)},  now : {now}')
        if int(start) + int(plus) <= now:
            answer.append(idx + 1)
    return answer