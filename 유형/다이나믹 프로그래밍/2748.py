# 2748 피보나치 수 2

import sys
input = sys.stdin.readline

n = int(input())

a, b = 0, 1 # 시작은 0, 1

if n == 0:
    print(0)

else:
    for i in range(2, n + 1):
        a, b = b, a + b
    # n = 2 : 0, 1 = 1, 1
    # n = 3 : 1, 1 = 1, 2
    # n = 4 : 1, 2 = 2, 3
    # ...

    print(b)