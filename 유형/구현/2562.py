import sys
input = sys.stdin.readline

arr = [int(input()) for _ in range(9)]
arr_max = max(arr)

print(arr_max)
print(arr.index(arr_max) + 1)