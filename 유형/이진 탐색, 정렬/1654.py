import sys
input = sys.stdin.readline

k, n = map(int, input().split())

lines = [int(input()) for _ in range(k)]
answer = 1 # 정답은 1부터

left = 1
right = 2 ** 31 - 1 # 전선 최대 길이

while left <= right:
    mid = (left + right) // 2
    # 현재 원하는 전선의 길이를 이진탐색 mid로
    cnt = 0

    for line in lines:
        cnt += line // mid
        # 각 전선을 원하는 길이로 나누고 조각 개수 합침
    if cnt >= n: # 전선조각 개수가 필요한 선 수 n 이상
        answer = mid # 원하는 길이가 맞는 길이다
        left = mid + 1
        # 왼쪽을 더 큰 쪽으로 좁힘
        # 만들 수 있는 최대 길이니까
    else:
        right = mid - 1
        # n개 이상 전선 못 만든다
        # 오른쪽을 더 작게 좁힘

print(answer)


