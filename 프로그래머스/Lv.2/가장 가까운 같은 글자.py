def solution(s):
    answer = []
    for idx, num in enumerate(s):
        flag = True
        for j in range(idx - 1, -1, -1):
            if s[j] == num:
                answer.append(idx - j)
                flag = False
                break
        if flag:
            answer.append(-1)
    return answer