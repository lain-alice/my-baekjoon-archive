import sys
input = sys.stdin.readline

N, M = map(int, input().split())

A = []
B = []

for i in range(N):
    x = list(map(int, input().split()))
    A.append(x)

for i in range(N):
    y = list(map(int, input().split()))
    B.append(y)

for i in range(N):
    for j in range(M):
        print(A[i][j] + B[i][j], end=' ')
    print()