import sys
input = sys.stdin.readline

N, K = map(int,input().split())
height = list(map(int,input().split()))

arr = []

for i in range(1, N):
    arr.append(height[i] - height[i - 1])


arr.sort(reverse = True)
print(sum(arr[K - 1:]))

# 각 애들 사이사이 차이…
# 제일큰애 작은애 차이랑 똑같다
# 3 4 5 사이사이 1씩 차이 = 5 - 3