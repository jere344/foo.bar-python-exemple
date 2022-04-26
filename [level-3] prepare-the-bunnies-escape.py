def solution(map):
    result = 999999
    # Anyway the list are only 20 x 20, the max lengh is smaller than this
    # It means that if un impossible maze is given(even with removing one wall)
    #   it will return 999999. math.inf would have been more fitting

    one_coord_list = []
    for y, k in enumerate(map):
        for x, e in enumerate(k):
            if e == 1:
                one_coord_list.append((x, y))
    path_size = BFS(map) + 1

    if path_size < result:
        result = path_size

    max_y = len(map) - 1
    max_x = len(map[0]) - 1
    for (x, y) in one_coord_list:
        neighbours = 0
        for (i, j) in [1, 0], [-1, 0], [0, 1], [0, -1]:
            if x + i > max_x or x + i < 0 or y + j > max_y or y + j < 0:
                neighbours += 1
            elif map[y + j][x + i] == 1:
                neighbours += 1

        if neighbours >= 3:
            continue
        # No need to test if it's surronded by 1s, it can only be a dead end

        if (x, y) == (0, 0) or (x, y) == (max_x, max_y):
            continue

        map[y][x] = 0
        # The bfs algorithme wasn't made by me, I just edited it to fit the situation
        # I could also have use a dijkstra algorithme, it would have been easier but less optimised
        # networkx.dijkstra_path_lenght can do that easily
        path_size = BFS(map) + 1  # +1 to account for the starting point
        map[y][x] = 1
        if path_size < result:
            result = path_size

    return result


from collections import deque

ROW = 9
COL = 10


class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y


class queueNode:
    def __init__(self, pt, dist):
        self.pt = pt
        self.dist = dist


def BFS(mat):
    src = Point(0, 0)
    dest = Point(len(mat) - 1, len(mat[0]) - 1)

    ROW = len(mat)
    COL = len(mat[0])

    def isValid(row, col):
        return (row >= 0) and (row < ROW) and (col >= 0) and (col < COL)

    if mat[src.x][src.y] != 0 or mat[dest.x][dest.y] != 0:
        return -1

    visited = [[False for _ in range(COL)] for _ in range(ROW)]
    visited[src.x][src.y] = True
    q = deque()
    s = queueNode(src, 0)
    q.append(s)

    while q:
        curr = q.popleft()
        pt = curr.pt
        if pt.x == dest.x and pt.y == dest.y:
            return curr.dist
        for i, j in [-1, 0], [1, 0], [0, -1], [0, 1]:
            row = pt.x + i
            col = pt.y + j

            if isValid(row, col) and mat[row][col] == 0 and not visited[row][col]:
                visited[row][col] = True
                Adjcell = queueNode(Point(row, col), curr.dist + 1)
                q.append(Adjcell)

    return 999998


# original BFS algorithm by stutipathak31jan
