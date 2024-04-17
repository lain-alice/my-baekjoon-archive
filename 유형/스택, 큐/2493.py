import sys
input = sys.stdin.readline

n = int(input())
towers = list(map(int, input().split()))

stack = []  # 레이저 수신한 탑 번호
result = [0] * n

for i in range(n):
    while stack and towers[stack[-1]] <= towers[i]:
        stack.pop()  # 현재 탑보다 낮은 탑을 스택에서 제거

    if stack:
        result[i] = stack[-1] + 1 # 레이저 수신한 탑 인덱스 저장

    stack.append(i) # 현재 탑 인덱스 스택에 추가

print(*result)