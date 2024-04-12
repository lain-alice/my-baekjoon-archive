import sys

input = sys.stdin.readline

t = int(input())

for i in range(t):
    word = input().strip()
    first = word[0]
    last = word[-1]

    if t == 1:
        print(f'{first}{first}')
    else:
        print(f'{first}{last}')
