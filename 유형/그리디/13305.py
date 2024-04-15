'''
그리디 알고리즘
비싼 곳에서 다음 주유소까지 최소한 채우고
싼 주유소에서 남은 거리에 필요한 기름 다 채우고?
아직 어렵다
'''

import sys
input = sys.stdin.readline

n = int(input())
road = list(map(int, input().split()))
price = list(map(int, input().split()))

min_price = price[0]  # 제일 싼 주유소 기름값
total = road[0] * price[0]  # 전체 기름값

for i in range(1, n - 1):  # 첫 번째 기름값은 이미 입력으로 받았음
    if price[i] < min_price:  # 현재 도시의 기름값이 최소보다 작으면
        min_price = price[i]  # 최소 비용 업데이트
    total += min_price * road[i]  # 전체

print(total)