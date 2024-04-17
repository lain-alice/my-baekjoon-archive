import sys
from heapq import *

input = sys.stdin.readline
INF = float('inf')


def dijkstra(start):
    dist = [INF] * (n + 1)
    dist[start] = 0

    heap = []
    heappush(heap, (0, start))

    while heap:
        cost, node = heappop(heap)
        if dist[node] < cost:
            continue

        for n_cost, n_node in graph[node]:
            n_cost += cost

            if n_cost < dist[n_node]:
                dist[n_node] = n_cost
                heappush(heap, (n_cost, n_node))

    dist.sort()
    for i in range(len(dist) - 1, -1, -1):
        if dist[i] != INF:
            return i + 1, dist[i] # 감염된 컴퓨터 수, 마지막 컴퓨터 감염 시간



T = int(input())

# 그래프 입력
for _ in range(T):
    n, d, c = map(int, input().split())
    graph = [[] for _ in range(n + 1)]

    for i in range(d):
        a, b, s = map(int, input().split())
        graph[b].append((s, a))

    print(*dijkstra(c))





