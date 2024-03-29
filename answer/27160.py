# 27160 할리갈리

import sys
N = int(sys.stdin.readline())
cards = {
    'STRAWBERRY' : 0,
    'BANANA' : 0,
    'LIME' : 0,
    'PLUM' : 0
}

for i in range(N) :
    fruit, count = sys.stdin.readline().split()
    cards[fruit] += int(count)

check = 5 in cards.values()
if check : print('YES')
else : print('NO')