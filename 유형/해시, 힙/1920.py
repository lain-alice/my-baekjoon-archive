import sys
from collections import defaultdict

input = sys.stdin.readline

n = int(input())
sources = list(map(int, input().split()))
visited = defaultdict(int) # 기본값이 정수인 딕셔너리

for source in sources:
    visited[source] = 1

m = int(input())
targets = list(map(int, input().split()))

for target in targets:
    print(visited[target])


# defaultdict 미사용

# import sys
# input = sys.stdin.readline
#
# n = int(input())
# sources = list(map(int, input().split()))
# visited = {}
#
# for source in sources:
#     visited[source] = 1
#
# m = int(input())
# targets = list(map(int, input().split()))
#
# for target in targets:
#     print(visited.get(target, 0))
    # 딕셔너리에서 키 반환, 키 없으면 0 반환

