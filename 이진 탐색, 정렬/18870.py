import sys
input = sys.stdin.readline

N = int(input())
nums = list(map(int, input().split()))

sorted_nums = sorted(list(set(nums)))

nums_index = {}
for i, num in enumerate(sorted_nums):
    nums_index[num] = i

answer = []
for num in nums:
    answer.append(nums_index[num])

print(*answer)

# 좌표 압축이 뭐냐?
# 값이 몇이든 상관없이 크기 순서만 따진다
# 중복은 없애고 순서 비교
# 비교해서 나온 인덱스를 원래 배열에 다시 적용

