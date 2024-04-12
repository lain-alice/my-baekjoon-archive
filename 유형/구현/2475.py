import sys

input = sys.stdin.readline

num = list(map(int, input().split()))


def square(n):
    return n ** 2


squared = list(map(square, num))

print(sum(squared) % 10)
