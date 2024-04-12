# 1152 단어의 개수

import sys
text = sys.stdin.readline().strip()

print(len(text.split()))

# 왜 split(' ')가 아니라 split()을 써야 했을까?