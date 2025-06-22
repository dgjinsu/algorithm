import sys
from collections import deque
input = sys.stdin.readline

# DNA 문자열 중 부분을 비밀번호로 사용
# 부분 문자열의 문자의 개수가 n개 이상
# A C G T

s, p = map(int, input().split())
dna = input().strip()
A, C, G, T = map(int, input().split())

def register_dna(c):
    if c == 'A':
        d[0] += 1
    if c == 'C':
        d[1] += 1
    if c == 'G':
        d[2] += 1
    if c == 'T':
        d[3] += 1

def remove_dna(c):
    if c == 'A':
        d[0] -= 1
    if c == 'C':
        d[1] -= 1
    if c == 'G':
        d[2] -= 1
    if c == 'T':
        d[3] -= 1

result = 0
d = [0, 0, 0, 0]
q = deque()

# 초기 큐 세팅 
for i in range(p):
    q.append(dna[i])
    register_dna(dna[i])

# 조건 만족 확인
if d[0] >= A and d[1] >= C and d[2] >= G and d[3] >= T:
    result += 1

for i in range(p, s):
    # 맨 앞 제거
    remove_dna(q.popleft())

    # 새로운 문자 추가
    q.append(dna[i])
    register_dna(dna[i])

    # 조건 만족 확인
    if d[0] >= A and d[1] >= C and d[2] >= G and d[3] >= T:
        result += 1

print(result)