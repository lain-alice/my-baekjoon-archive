import sys
input = sys.stdin.readline

m, n = map(int, input().split())
board = [list(input().split()) for _ in range(m)]

print(board)