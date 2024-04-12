import sys
input = sys.stdin.readline

def spread():
    """
    미세 먼지 확산 결과 반환 함수
    """
    dx = [1, -1, 0, 0]
    dy = [0, 0, 1, -1]
    new_board = [[0] * c for _ in range(r)]
    new_board[ccw][0] = -1
    new_board[cw][0] = -1
    for x in range(r):
        for y in range(c):
            if board[x][y] > 0:
                new_board[x][y] += board[x][y]
                for d in range(4):
                    nx = x + dx[d]
                    ny = y + dy[d]
                    if 0 <= nx < r and 0 <= ny < c and board[nx][ny] != -1:
                        new_board[nx][ny] += board[x][y] // 5
                        new_board[x][y] -= board[x][y] // 5
    return new_board


def rotate():
    """
    미세 먼지 순환 함수
    """
    # 위쪽 순환: 반시계 방향
    for x in range(ccw - 1, 0, -1):
        board[x][0] = board[x - 1][0]
    for y in range(c - 1):
        board[0][y] = board[0][y + 1]
    for x in range(ccw):
        board[x][-1] = board[x + 1][-1]
    for y in range(c - 1, 0, -1):
        board[ccw][y] = board[ccw][y - 1]

    # 아래쪽 순환: 시계 방향
    for x in range(cw + 1, r - 1):
        board[x][0] = board[x + 1][0]
    for y in range(c - 1):
        board[-1][y] = board[-1][y + 1]
    for x in range(r - 1, cw, -1):
        board[x][-1] = board[x - 1][-1]
    for y in range(c - 1, 0, -1):
        board[cw][y] = board[cw][y - 1]

    # 공기청정기에서 나온 바람은 미세 먼지가 없는 바람이므로 0으로 초기화
    board[ccw][1] = 0
    board[cw][1] = 0


r, c, t = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(r)]
for i in range(r):
    if board[i][0] == -1:
        ccw, cw = i, i + 1
        break
for _ in range(t):
    board = spread()
    rotate()
print(sum([sum(line) for line in board]) + 2) # 공기청정기 -1 * 2 고려