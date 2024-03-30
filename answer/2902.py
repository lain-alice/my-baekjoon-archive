import sys
input = sys.stdin.readline().strip()

name = input.split('-')
initial = ''

for i in range(len(name)):
    initial += name[i][0]


print(initial)