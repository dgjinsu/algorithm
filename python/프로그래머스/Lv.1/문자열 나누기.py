def solution(s):
    idx = 0
    x_idx = 0
    x_cnt, other_cnt = 0, 0
    result = []
    while True:
        flag = False
        x = s[x_idx]
        if s[idx] == x:
            x_cnt += 1
        else:
            other_cnt += 1
        
        if x_cnt == other_cnt:
            tmp = s[x_idx:idx+1]
            result.append(tmp)
            x_idx = idx + 1
            flag = True
        idx += 1
        if idx == len(s):
            if not flag:
                result.append(s[x_idx:])
            break
    
    return len(result)