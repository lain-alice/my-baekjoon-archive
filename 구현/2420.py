import sys
input = sys.stdin.readline

N, M = map(int, input().split())

if N > M:
    print(N - M)
else:
    print(M - N)