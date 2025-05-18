import sys
input = sys.stdin.readline

n = int(input())
persons = set()
cnt = 0
for _ in range(n):
    c = input().strip()
    if c == "ENTER":
        persons = set()
    else:
        if c not in persons:
            cnt += 1
            persons.add(c)

print(cnt)