import sys
from collections import deque

input = sys.stdin.readline

n = int(input())

balloons = list(map(int, input().split()))

circle = deque([(index + 1, balloons[index]) for index in range(n)])
# 종이 번호와 풍선 순서(+1)

while circle:
    index, num = circle.popleft()
    print(index, end=" ")

    if not circle:
        break

    if num > 0:
        num -= 1

    for _ in range(abs(num)):
        if num > 0:
            circle.append(circle.popleft())
        else:
            circle.appendleft(circle.pop())



