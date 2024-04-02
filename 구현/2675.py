# 2675 문자열 반복

import sys
T = int(sys.stdin.readline())

for _ in range(T):
    R, S = sys.stdin.readline().split()
    R = int(R)

    for i in S:
        print(i * int(R), end='')
        print()