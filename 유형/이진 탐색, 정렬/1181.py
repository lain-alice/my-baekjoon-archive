import sys
input = sys.stdin.readline

n = int(input())
words = {input().rstrip() for _ in range(n)} # set으로 중복 제거
words = list(words) # 정렬 위해 다시 리스트로

words.sort(key=lambda x: (len(x), x))
# 길이 순서대로 정렬하고 나서 사전순으로 정렬

for word in words:
    print(word)