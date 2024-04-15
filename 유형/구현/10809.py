import sys
from string import ascii_lowercase

input = sys.stdin.readline
alphabet = ascii_lowercase

s = input().rstrip()

for i in alphabet:
    print(s.find(i), end=' ')
