import sys
input = sys.stdin.readline

N, M = map(int, input().split())

unheard = []
unseen = []

for i in range(N):
    x = input()
    unheard.append(x)

for i in range(M):
    y = input()
    unseen.append(y)

unseen_unheard = list(set(unseen) & set(unheard))
unseen_unheard.sort()

count = len(unseen_unheard)

print(count)
print(''.join(unseen_unheard), end = '')
