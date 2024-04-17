import sys
from heapq import heappush, heappop

input = sys.stdin.readline
INF = float('inf')


def dijikstra(start):
    dist = [INF] * len(graph)
    dist[start] = 0
    q = [(0, start)]
    while q:
        cost, idx = heappop(q)
        if dist[idx] < cost:
            continue

        for adj, d in graph[idx]:
            if dist[adj] > cost + d:
                dist[adj] = cost + d
                heappush(q, (dist[adj], adj))

    return dist


n, m = map(int, input().split())
k = int(input())

# 그래프 입력
graph = [[] for _ in range(n + 1)]
for _ in range(m):
    a, b, c = map(int, input().split())
    graph[a].append((b, c))

# 다익스트라 적용
distance = dijikstra(k)
for i in range(1, n + 1):
    print(distance[i] if distance[i] != INF else "INF")
