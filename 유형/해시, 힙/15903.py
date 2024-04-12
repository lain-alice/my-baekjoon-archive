from heapq import *

n, m = map(int, input().split())
heap = []
for value in list(map(int, input().split())):
    heappush(heap, value)
    # 카드 묶음

for _ in range(m):
    # 카드 한 장씩 뽑는다
    x = heappop(heap)
    y = heappop(heap)

    # 합체, 합체
    heappush(heap, (x + y))
    heappush(heap, (x + y))

print(sum(heap))