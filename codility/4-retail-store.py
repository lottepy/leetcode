# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")

# import numpy as np
def solution(K, A):
    # write your code in Python 3.6
    # nonzeros = np.nonzero(A)
    nonzeros = nonzero(A)
    rows = [n[0] for n in nonzeros]
    cols = [n[1] for n in nonzeros]
    cells = valid_cells(rows[0], cols[0], K, A)
    for i in range(1, len(rows)):
        tmp = valid_cells(rows[i], cols[i], K, A)
        cells = list(set(tmp).intersection(set(cells)))
    return len(cells)
            
def valid_cells(i, j, K, A):
    res = []
    for m in range(-K, K+1):
        for n in range(-K + abs(m), K-abs(m)+1):
            row = min(max(i + m, 0), len(A)-1)
            col = min(max(j + n, 0), len(A[0])-1)
            res.append((row, col))
    cells = list(set(res))
    cells.remove((i, j))
    # print("****({},{})****".format(i,j))
    # print(cells)
    return cells

def nonzero(two_dim_l):
    return [(i, j) for i in range(len(two_dim_l)) for j in range(len(two_dim_l[0])) if two_dim_l[i][j] != 0]


if __name__ == '__main__':
    print(solution(K=4, A=[[0, 0, 0, 1], [0, 1, 0, 0], [0, 0, 1, 0], [1, 0, 0, 0], [0, 0, 0, 0]]))
