import sys
input = sys.stdin.readline

# a~z, 0~9 ' ' < >
# 시작과 끝은 공백 X
# < 가 먼저 등장해야하고 > 가 번갈아가면서 등장해야 한다. 두 문자의 개수도 같다 

# < > 사이에는 a~z와 공백만 있음
# 단어는 a~z와 숫자

s = input().strip()

parts = []

tmp = ""
is_tag = False
for i in range(len(s)):
    # < 를 찾으면 > 를 찾을 때까지 읽고 태그를 parts.append() / 0은 태그 1은 단어
    # < 를 찾지 않았다면 쭉 읽다가 공백을 만나거나 다음 < 를 만날 때 까지. 만나고 나면 parts.append() 
    if s[i] == '<':
        if len(tmp) > 0:
            parts.append([tmp, 1])
        tmp = ""
        is_tag = True
        tmp += s[i]
        continue
    if s[i] == '>':
        is_tag = False
        tmp += s[i]
        parts.append([tmp, 0])
        tmp = ""
        continue        

    if not is_tag:
        if s[i] == ' ':
            parts.append([" " + tmp, 1])
            tmp = ""
        else:
            tmp += s[i]
    else:
        tmp += s[i]

    if i == len(s) - 1:
        parts.append([tmp, 1])

result = ""
for part in parts:
    if part[1] == 0:
        result += part[0]
    else:
        tmp = ""
        for i in range(len(part[0]) - 1, -1, -1):
            tmp += part[0][i]
        result += tmp

print(result)