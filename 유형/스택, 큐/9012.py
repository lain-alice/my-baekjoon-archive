import sys
input = sys.stdin.readline

t = int(input())

# 열린 괄호는 닫혀야 VPS
# 스택은 프링글스통, 처음 넣은 과자 마지막에 먹는다(선입후출)
# 스택 안에 ( 쌓여있으면 ) 와 만나야 없어지게 한다, 테트리스처럼
# 괄호끼리 만나서 모두 없어지면 YES 남으면 NO

for i in range(t):
    ps = input()
    stack = []

    for j in ps:
        if j == '(':
            stack.append(j)
        elif j == ')':
            if stack: # ( 만 먼저 스택에 넣었다. 스택이 true면 무조건 ( 만 들어있으니까 ) 만나면 pop
                stack.pop()
            else: # ) 만나서 ( 터졌는데도 ( 남아있으면 NO
                print("NO")
                break
    else:
        if not stack: # 괄호 다 터져서 스택 비었으면
            print("YES")
        else: # 스택에 괄호 남아있으면
            print("NO")