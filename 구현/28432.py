import sys
input = sys.stdin.readline

N = int(input())
S = []
answer = ''

for i in range(N):
    S += input().split()

M = int(input())
A = []

for i in range(M):
    A += input().split()

    if S[0] == '?' and len(S) == 1: 
        answer = A[0]

    elif S[0] == '?' and A[i].endswith(S[1][0]) and A[i] not in S:
        answer = A[i]

    elif S[-1] == '?' and A[i].startswith(S[-2][-1]) and A[i] not in S:
        answer = A[i]
    else:
        for j in range(1, N - 1):
            if S[j] == '?':
                
                if A[i].startswith(S[j - 1][-1]) and A[i].endswith(S[j + 1][0]) and A[i] not in S:
                    answer = A[i]
                
print(answer)