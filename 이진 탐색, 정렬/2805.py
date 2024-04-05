import sys
input = sys.stdin.readline

n, m = map(int, input().split())
trees = list(map(int, input().split()))

# 자른 목재 길이 합
def wood(mid):
    sum = 0
    for i in trees:
        if i > mid:
            sum += (i - mid)
    return sum

left = 0
right = 1000000000
answer = 0

while left <= right:
    mid = (left + right) // 2
    total = wood(mid)

    # 계산된 나무 길이 총합이 m보다 크거나 같으면
    if total >= m:
        answer = mid
        left = mid + 1
    # 총합이 작으면 범위 좁힌다
    else:
        right = mid - 1

print(answer)


# 이진 탐색
# 원하는 숫자보다 크면 오른쪽, 작으면 왼쪽으로 좁혀가며 찾기

# 나무 길이, 절단기 높이, 싹둑...
# (나무 - 절단기), 목재 길이의 합이 m
# 이 목재 길이 합을 가지고 이진탐색 돌린다
