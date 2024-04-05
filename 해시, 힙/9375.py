import sys
input = sys.stdin.readline

t = int(input())

for _ in range(t):
    cloth = {}
    n = int(input())
    for _ in range(n):
        name, type = input().split()
        if type not in cloth:
            # 옷장에 옷 종류 없으면 새로 추가
            cloth[type] = 1
        else:
            # 종류 있으면 종류별 의상 수만 추가
            cloth[type] += 1

    cnt = 1

    for val in cloth.values():
        # 알몸도 옷 1벌로 치고 계산
        cnt *= val + 1
    # 알몸 다시 제외
    print(cnt - 1)
