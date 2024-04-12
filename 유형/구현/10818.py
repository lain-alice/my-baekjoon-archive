import sys
input = sys.stdin.readline

n = int(input())
num = list(map(int, input().split()))

answer = [min(num), max(num)]

print(*answer)
