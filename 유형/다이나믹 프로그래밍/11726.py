# 11726 2xn 타일링

import sys
input = sys.stdin.readline

n = int(input())

dp = [0] * 1001 # 1부터 1000
dp[1] = 1 # 2x1
dp[2] = 2 # 2x2

for i in range(3, n + 1):
    dp[i] = (dp[i - 1] + dp[i - 2]) % 10007
    # i번째 방법 수는 i-2번째랑 i-3번째 수의 합...

print(dp[n])

# 2x1 1개
# 2x2 가가 세세 2개
# 2x3이 1번 방법수, 2번 방법수 합이 되어야 함
# 2x4는 2번+3번.....

