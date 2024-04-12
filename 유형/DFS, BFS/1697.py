import sys
from collections import deque

input = sys.stdin.readline

n, k = map(int, input().split())
visited = [0] * (100000 + 1)
# 0부터 10만까지의 점 중 방문한 곳 소요시간

# bfs: 처음꺼 큐에 넣었다 빼고 연결된 것들 큐에 담고
# 두번째 빼고 걔랑 연결된 것들 큐에 담고...반복

def bfs(start):
    queue = deque()
    queue.append(start)

    # 첫 위치 큐에 넣는다

    while queue:
        cur = queue.popleft()
        # 큐에 뭐가 있으면 앞에꺼 꺼낸다, 꺼낸 게 현위치
        if cur == k:
            return visited[k]
        # 현위치가 k 되면 점 k 방문 소요시간 출력

        # 현위치 +1, -1, x2 중 하나가 다음 위치
        for next in (cur + 1, cur - 1, cur * 2):
            if 0 <= next <= 100000 and not visited[next]:
                # 다음 위치가 점 범위 사이고 방문 안했으면
                visited[next] = visited[cur] + 1
                # 다음 점 방문 소요시간은 현재 점 시간 + 1초
                queue.append(next)
                # 큐에 추가, 이제 다음위치가 현위치

# 시작 5 큐에 넣고 뺀다, 현위치 5, 점[5] 소요시간 0(시작이니까)
# 다음 위치 5+1=6, 5-1=4, 5x2=10, 다 범위 안이고 아직 방문 안했음
# 점 [4], [6], [10]의 소요시간 = 점[5] + 1, 이제 4, 6, 10 큐에 넣는다
# 6에서 7 5 12 -> 7 12
# 4에서 5 3 8, 5는 이미 들렀으니 3 8
# 10에서 11 9 20
# 3에서 4 2 6 -> 2
# 8에서 9 7 16 -> 16
# 16에서 18, '17', 32

print(bfs(n))


