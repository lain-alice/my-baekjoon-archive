import sys
input = sys.stdin.readline

n = int(input())

if n == 1:
    print(f'1 bottle of beer on the wall, 1 bottle of beer.')
    print(f'Take one down and pass it around, no more bottles of beer on the wall.\n')
    print(f'No more bottles of beer on the wall, no more bottles of beer.')
    print(f'Go to the store and buy some more, 1 bottle of beer on the wall.')

else:
    for i in range(n, 0, -1):
        if i == 2:
            print(f'{i} bottles of beer on the wall, {i} bottles of beer.')
            print(f'Take one down and pass it around, {i - 1} bottle of beer on the wall.\n')

        elif i == 1:
            print(f'{i} bottle of beer on the wall, {i} bottle of beer.')
            print(f'Take one down and pass it around, no more bottles of beer on the wall.\n')
            print(f'No more bottles of beer on the wall, no more bottles of beer.')
            print(f'Go to the store and buy some more, {n} bottles of beer on the wall.')

        else:
            print(f'{i} bottles of beer on the wall, {i} bottles of beer.')
            print(f'Take one down and pass it around, {i - 1} bottles of beer on the wall.\n')

