import sys
input = sys.stdin.readline

n, m = map(int, input().split())
desk = [int(input().rstrip()) for _ in range(n)]

mn = min(desk)
mx = max(desk) * m
result = mx

while mn <= mx:
    md = (mn + mx) // 2

    count = 0

    for i in desk:
        count += md // i

    if m <= count:
        mx = md - 1
        result = min(result, md)
    else:
        mn = md + 1

print(result)

# 걸리는 시간 말고 k시간동안 심사할 수 있는 인원을 기준으로
# 이진 탐색...최대 인원이 m명 될 때까지 범위 좁힌다
# 최소: 한 명이 제일 빠른 심사대에서
# 최대: 전원이 제일 느린 심사대에서