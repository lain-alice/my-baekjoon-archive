import sys
input = sys.stdin.readline

n = int(input())
num_list = list(map(int, input().split()))

dp = [1] * n
# 0부터 i까지 찾은, i번째 요소를 사용한 가장 긴 증가하는 부분수열 길이

for i in range(n):
    for j in range(i): # i 이전의 값 비교
        if num_list[i] > num_list[j]: # i번째가 j번째보다 크다면
            dp[i] = max(dp[i], dp[j] + 1) # dp[i]와 dp[j] + 1 중 큰 값을 dp[i]에 저장

print(max(dp))
