import sys
input = sys.stdin.readline

N = int(input())
switch = [2] + list(map(int, input().split()))

M = int(input())

for _ in range(M):
    gender, num = map(int, input().split())

    if gender == 1:
        for i in range(1, N // num + 1):
            if switch[i * num] == 0:
                switch[i * num] = 1
            elif switch[i * num] == 1:
                switch[i * num] = 0

    if gender == 2:
        if switch[num] == 0:
            switch[num] = 1
        elif switch[num] == 1:
            switch[num] = 0

        for j in range(N // 2):
            if num - j < 1 or num + j > N:
                break

            if switch[num - j] == switch[num + j]:
                if switch[num - j] == 0:
                    switch[num - j] = 1
                elif switch[num - j] == 1:
                    switch[num - j] = 0

                if switch[num + j] == 0:
                    switch[num + j] = 1
                elif switch[num + j] == 1:
                    switch[num + j] = 0
            else: break

for k in range(1, N + 1):
    print(switch[k], end=' ')
    if k % 20 == 0:
        print()
