x, y = map(int, input().split())
z = (100 * y) // x
left, right = 0, x

if z >= 99: # 승률이 99%면 더 안 오른다
    print(-1)

else:
    while left <= right:
        mid = (left + right) // 2

        if (100 * (y + mid) // (x + mid)) > z:
            answer = mid
            right = mid - 1 # 최소 몇 번, 많이 이겼으면 줄인다
        else:
            left = mid + 1 # Z 변할 때까지 늘린다
    print(answer)

# 최소 몇 판 더 해서 승률 바뀌는 부분 찾는다? 이진탐색, 범위 좁히기
# 승률 계산의 오차를 피하려면 분자에 100을 곱하고 전체 판수 나누기 -> 정수 연산
# 승률은 정수. 몫

