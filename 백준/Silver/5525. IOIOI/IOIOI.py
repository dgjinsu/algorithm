import sys
from collections import deque
input = sys.stdin.readline


# I : N+1개  |  O : N개
# Pn = I O 가 교대로 나오는 문자열
# I O로만 이뤄진 문자열이 주어질 때 이 문자열 안에 Pn이 몇군데 포함되어 있는지

# N이 2일 때: IOIOI
# N이 3일 때: IOIOIOI

# 1중 for문

# OOIOIOIOIIOII

# IOI
n = int(input())
m = int(input())
s = input().strip()
q = deque()

result = 0

for i in range(m):
    # 비어있으면 넣음
    if len(q) == 0:
        q.append(s[i])
        # print(f'비어있어서 값 넣음. q: {q}')

    # 비어있지 않으면
    else:
        # 넣을 때 이전꺼랑 다른지 확인
        if q[-1] != s[i]:
            q.append(s[i])
            # print(f'가장 마지막 값이랑 달라서 넣음 q: {q}')
            if len(q) == (2 * n + 1):
                result += 1
                # print(f'꽉 차서 카운트 증가시키고 2개 지울 예정. q: {q}, result: {result}')
                q.popleft()
                q.popleft()
                # print(f'지우고 나서: {q}')
        else: # 같으면 초기화
            # print(f'같은거 들어옴. 현재 q: {q} 새로 들어오는 값: {s[i]}')
            q.clear()
            q.append(s[i])

    # 맨 앞이 I가 아니면 지움
    if q[0] != 'I':
        q.popleft()
        # print(f'맨 앞이 I가 아니라서 지움. q: {q}')

print(result)