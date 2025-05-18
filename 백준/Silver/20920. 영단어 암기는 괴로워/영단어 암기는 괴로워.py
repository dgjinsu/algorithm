import sys
input = sys.stdin.readline

n, m = map(int , input().split())
words = []

for _ in range(n):
    word = input().strip()
    if len(word) >= m:
        words.append(word)

cnt_map = dict()
for word in words:
    if word in cnt_map:
        cnt_map[word] += 1
    else:
        cnt_map[word] = 1

words.sort(key = lambda x : (-cnt_map[x], -len(x), x))

print_set = set()
for word in words:
    if word not in print_set:
        print(word)
        print_set.add(word)