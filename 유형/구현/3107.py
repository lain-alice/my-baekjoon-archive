import sys
input = sys.stdin.readline

ipv6 = input().strip()
shorten = ipv6.split(":")
full = []

if len(shorten) == 8:
    for i in range(8):
        full.insert(i, shorten[i])

        if len(full[i]) != 4:
            for j in range(4 - len(full[i])):
                full[i] = '0' + full[i]

    print(*full, sep=":")

else:
    half = ipv6.split("::")

    half1 = []
    half2 = []

    if len(half[0]) >= len(half[1]):
        half1 = half[0].split(':')

        for _ in range(7 - len(half1)):
            half2.append('')
        half2.append(half[1])

        full = half1 + half2

    elif len(half[0]) < len(half[1]):
        half2 = half[1].split(':')

        half1.append(half[0])
        for _ in range(7 - len(half2)):
            half1.append('')

        full = half1 + half2

    for i in range(8):
        if len(full[i]) != 4:
            for j in range(4 - len(full[i])):
                full[i] = '0' + full[i]
        else:
            continue

    print(*full, sep=":")

# 스플릿 : 했을 때 빈칸 하나 있으면 :: 있는거
# 스플릿 한번만 하고 그거 length 기준으로 해봐라
# 1, 3번 문제 괜찮음
# 예외처리 x, 문자열 파싱 조건 명확히 딱