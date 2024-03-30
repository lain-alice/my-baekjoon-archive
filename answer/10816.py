# 10816 숫자 카드 2

N = int(input())
cards = list(map(int, input().split()))
M = int(input())
nums = list(map(int, input().split()))

count = {}
for card in cards:
    if card in count:
        count[card] += 1
    else:
        count[card] = 1

for num in nums:
    result = count.get(num)
    if result == None:
        print(0, end = " ")
    else:
        print(result, end = " ")