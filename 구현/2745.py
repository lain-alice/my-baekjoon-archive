# import sys
# input = sys.stdin.readline().strip()

# from string import ascii_uppercase

# N, B = input.split(' ')
# B = int(B)

# letter_list = list('0123456789' + ascii_uppercase)
# num_list = list(range(36))
# decimal = 0

# for i, char in enumerate(N):
#     letter_num = letter_list.index(char)
#     decimal += (num_list[letter_num] * (B ** (len(N) - 1 - i)))

# print(decimal)


import sys
input = sys.stdin.readline().strip()

N, B = input.split(' ')
B = int(B)

decimal = int(N, B)

print(decimal)