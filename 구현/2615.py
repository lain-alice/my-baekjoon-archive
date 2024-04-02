import sys
input = sys.stdin.readline

board = [list(map(int, input().split())) for _ in range(19)]

dx = [0, 1, 1, -1]
dy = [1, 0, 1, 1]

def game():

    for x in range(19):
        for y in range(19):
            if board[x][y]:
                for i in range(4):
                    nx = x + dx[i]
                    ny = y + dy[i]
                    cnt = 1

                    if nx < 0 or ny < 0 or nx >= 19 or ny >= 19:
                        continue

                    while 0 <= nx < 19 and 0 <= ny < 19 and board[x][y] == board[nx][ny]:
                        cnt += 1

                        if cnt == 5:
                            if 0 <= nx + dx[i] < 19 and 0 <= ny + dy[i] < 19 and board[nx][ny] == board[nx + dx[i]][ny + dy[i]]:
                                break
                            if 0 <= x - dx[i] < 19 and 0 <= y - dy[i] < 19 and board[x][y] == board[x - dx[i]][y - dy[i]]:
                                break

                            return board[x][y], x + 1, y + 1

                        nx += dx[i]
                        ny += dy[i]

    return 0, -1, -1

b_or_w, a, b = game()

if not b_or_w:
    print(b_or_w)
else:
    print(b_or_w)
    print(a, b)
