import sys
input = sys.stdin.readline

n, m = map(int, input().split())
pokedex = {}
dex_no = {}

for i in range(n):
    pokemon = input().rstrip()
    pokedex[pokemon] = (i + 1) # 이상해씨 : 도감 번호 001
    dex_no[i + 1] = pokemon # 001 : 이상해씨

for i in range(m):
    question = input().rstrip()
    if question.isdigit(): # isdigit : 숫자로만 된 문자열 판별
        print(dex_no[int(question)])
    elif question.isalpha(): # isalpha : 알파벳으로만 돼있는지
        print(pokedex[question])

