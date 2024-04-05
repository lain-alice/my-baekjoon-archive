import sys
input = sys.stdin.readline

n = int(input())
row = list(map(int, input().split()))

row.sort()

answer = 0

for i in range(1, n + 1): # 첫번째 사람 1로 치니까 인덱스 + 1
    answer += sum(row[: i])
    # 1부터 i까지의 합을 answer에 계속 더함
    # 1 1+2 1+2+3...

print(answer)


# 3, 3 1, 3 1 4...
# 앞에 오래 걸리는 사람 있을 수록 모두의 대기시간 합 크다
# 그냥 빨리 끝나는 애부터 순서대로
