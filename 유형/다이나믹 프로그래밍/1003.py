import sys
input = sys.stdin.readline

t = int(input())

# arr = [int(input()) for _ in range(t)]
for _ in range(t):
    n = int(input())
    a, b = 1, 0

    for i in range(n):
        a, b, = b, a + b
    print(a, b)

# def fibonacci(n):
#     if n == 0:
#         return 0
#     elif n == 1 or n == 2:
#         return 1
#     else:
#         return fibonacci(n - 1) + fibonacci(n - 2)

# n = 2면 0 1번 1 1번
# n = 3 / f(3) = f(2) + f(1) / 1번, 2번 (f(1)은 1이니까)
# n = 4 / f(4) = f(3) + f(2) / 2번, 3번
# 호출수 자체도 피보나치 수열, 0 호출 수는 0부터 피보나치, 1 호출 수는 1부터 피보나치