import sys
input = sys.stdin.readline

# 시리얼 번호 : A~Z , 0~9
# 앞에 오는 경우
# 1. 길이 짧은거
# 2. 길이 같다면 자리수의 합이 작은것
# 3. 길이 같고 자리수의 합도 같다면 알파벳 오름차순

n = int(input())
serials = []

for _ in range(n):
    serials.append(input().strip())

def custom_sort(s):
    l = len(s)
    
    serial_sum = 0
    for c in s:
        if '0' <= c <= '9':
            serial_sum += (ord(c) - ord('0'))

    return (l, serial_sum, s)

serials.sort(key = custom_sort)

print('\n'.join(serials))