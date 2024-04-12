import sys
from heapq import *

input = sys.stdin.readline

n = int(input())
heap = []

for _ in range(n):
    row = list(map(int, input().split()))
    # 이차원 배열의 행
    for i in row:
        if len(heap) < n:
            # 힙 길이 n 될 때까지 행의 요소를 하나씩 heap에 추가
            heappush(heap, i)
        else:
            # 길이 n 되면
            if i > heap[0]:
                # heap 최솟값 날리고 다른 행 요소 추가
                heappop(heap)
                heappush(heap, i)

print(heap[0])
