import sys
from heapq import *

input = sys.stdin.readline

n = int(input())
heap = []

for _ in range(n):
    a = int(input())
    if a: # 0은 false니까
        heappush(heap, a)
    elif len(heap) == 0:
        print(0)
    else:
        print(heappop(heap))



