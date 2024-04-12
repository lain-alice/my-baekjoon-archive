import sys
input = sys.stdin.readline
sys.setrecursionlimit(10 ** 9)
# 재귀 한도 해제

N, M, R = map(int, input().split())
# 정점 수, 간선 수, 시작 정점
graph = [[] for _ in range(N + 1)]
path = []
result = [0] * (N + 1)
visited = [-1] * (N + 1)

for _ in range(M):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

for i in range(1, len(graph)):
    graph[i].sort()

def dfs(start):
    visited[start] = 1
    path.append(start)

    # 노드가 조회되면 dfs 함수가 호출됨

    for adj_node in graph[start]:
        if visited[adj_node] == -1:
            dfs(adj_node)

    return


dfs(R)

for idx, node in zip(range(1, len(path) + 1), path):
    result[node] = idx

print(*result[1:], sep="\n")