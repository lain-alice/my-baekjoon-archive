import sys
from collections import deque

input = sys.stdin.readline
sys.setrecursionlimit(10 ** 6)

# 입력 받기
N, M, R = map(int, input().split())  # 정점의 수, 간선의 수, 시작 정점
graph = [[] for _ in range(N + 1)]  # 첫번째부터 시작
visited = [0] * (N + 1)  # 각 정점 방문 여부
cnt = 1

# 간선 정보를 2차원 배열로
for _ in range(M):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)  # ab, ba 양방향

for i in range(N + 1):
    graph[i].sort()


def bfs(start):
    global cnt
    queue = deque([start])
    visited[start] = cnt

    while queue:
        v = queue.popleft()
        for i in graph[v]:  # 현재 노드와 연결된 각 노드에 대해 반복
            if not visited[i]:  # 방문하지 않은 노드인 경우 큐에 추가함
                cnt += 1  # 방문 순서 증가
                visited[i] = cnt
                queue.append(i)


bfs(R)

for i in range(1, N + 1):
    print(visited[i])