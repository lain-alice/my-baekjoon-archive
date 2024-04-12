import sys
from itertools import combinations

input = sys.stdin.readline

n, s = map(int, input().split())
arr = list(map(int, input().split()))
cnt = 0

# 부분수열... 수열에서 일부분만 뽑아내서 만들 수 있는 모든 수열?

for i in range(1, n+1):
    part = combinations(arr, i)
    # 나올 수 있는 모든 부분수열?

    for x in part:
        if sum(x) == s:
            # 부분수열 중 전체 합이 s인 것
            cnt += 1

print(cnt)