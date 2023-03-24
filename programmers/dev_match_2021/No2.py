directions = [[0, 1], [1, 0], [0, -1], [-1, 0]]


def solution(rows, columns, queries):
    answer = []

    # init board
    board = [[0 for j in range(columns + 1)] for i in range(rows + 1)]

    for i in range(1, len(board)):
        for j in range(1, len(board[i])):
            board[i][j] = (i - 1) * columns + j
    ### end init board ###

    for x1, y1, x2, y2 in queries:
        now_min = 10000
        nx, ny = x1, y1
        tmp_num = board[x1][y1]
        for dx, dy in directions:
            while x1 <= nx + dx <= x2 and y1 <= ny + dy <= y2:
                nx, ny = nx + dx, ny + dy

                tmp_num, board[nx][ny] = board[nx][ny], tmp_num

                now_min = now_min if (now_min < tmp_num) else tmp_num

        answer.append(now_min)

    return answer


ROWS = [6, 3, 100]
COLUMNS = [6, 3, 97]
QURIES = [
    [[2, 2, 5, 4], [3, 3, 6, 6], [5, 1, 6, 3]],
    [[1, 1, 2, 2], [1, 2, 2, 3], [2, 1, 3, 2], [2, 2, 3, 3]],
    [[1, 1, 100, 97]]
]

for i in range(3):
    print(solution(ROWS[i], COLUMNS[i], QURIES[i]))
