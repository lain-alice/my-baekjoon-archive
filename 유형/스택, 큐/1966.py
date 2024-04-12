# 큐는 말 그대로 줄 서기, 먼저 온 애가 먼저 간다(선입선출)
# 프린트 순서는 큐, 대신 명령 순서 말고 중요도

from collections import deque
import sys
input = sys.stdin.readline

t = int(input())

for _ in range(t):
    printer = deque()
    n, m = map(int, input().split())  # 6 0
    docs = list(map(int, input().split()))  # [1, 1, 9, 1, 1, 1]

    for index, prior in enumerate(docs):
        printer.append((prior, index))  # [(1, 0), (1, 1), (9, 2)...]

    docs.sort()  # [(1, 0), (1, 1),... (9, 2)] 문서가 중요도 순서대로 정렬됨
    cnt = 0

    while printer:  # 프린터에 문서가 있으면
        prior, index = printer.popleft()  # 인쇄 대기중 문서
        if prior != docs[-1]:  # 대기문서 중요도 최상 아니면
            printer.append((prior, index))  # 맨 뒤로 뺀다
        else:
            cnt += 1
            docs.pop()
            if index == m:
                print(cnt)
                break
