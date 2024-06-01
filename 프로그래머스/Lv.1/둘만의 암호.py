def solution(s, skip, index):
    answer = ''
    skip_set = set()
    for i in skip:
        skip_set.add(i)
    
    for i in s:
        j = index
        while(j):
            i = chr(ord(i) + 1)
            if i in skip_set:
                continue
            j -= 1
        if i > "z":
            i = chr(ord(i) - 26)
        answer += i

    
    return answer