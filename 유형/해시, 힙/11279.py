import sys
from heapq import *

input = sys.stdin.readline

n = int(input())
heap = []

for _ in range(n):
    a = int(input())

    if a: # 마이너스 했을 때 최소인 게 최대니까
        heappush(heap, -a) # - 붙이고

    elif len(heap) == 0:
        print(0)

    else:
        print(heappop(heap) * -1) # - 뗌

