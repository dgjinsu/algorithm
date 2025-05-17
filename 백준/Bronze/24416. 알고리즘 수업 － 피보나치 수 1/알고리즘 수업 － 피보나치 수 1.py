import sys
input = sys.stdin.readline

cnt1, cnt2 = 0, 0
def fib(n):
    global cnt1
    if n == 1 or n == 2:
        cnt1 += 1
        return 1
    else:
        return fib(n-1) + fib(n-2)
    
def fibonacci(n):
    global cnt2
    f = [1] * n
    for i in range(2, n):
        f[i] = f[i - 1] + f[i - 2]
        cnt2 += 1

n = int(input())
fib(n)
fibonacci(n)

print(f'{cnt1} {cnt2}')