import sys
input = sys.stdin.readline

n = int(input())
m = input().rstrip()
answer = 0

for i in range(n):
    answer += int(m[i])

print(answer)
