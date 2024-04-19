def solution(keymap, targets):
    answer = []
    m = {}
    for key in keymap:
        for idx, alpha in enumerate(key):
            if alpha in m:
                if m[alpha] <= idx:
                    continue
            m[alpha] = idx + 1
    for target in targets:
        flag = True
        result = 0
        for i in target:
            if i in m:
                result += m[i]
            else:
                answer.append(-1)
                flag = False
                break
        if flag:
            answer.append(result)
    return answer