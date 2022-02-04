# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")
from itertools import combinations
def solution(X, Y):
    # write your code in Python 3.6
    points = [(X[i], Y[i], i) for i in range(len(X))]
    cb = list(combinations(points, 3))
    nonzeros = [c + (calc_area(c[0], c[1], c[2]),) for c in cb if calc_area(c[0], c[1], c[2]) != 0.0]
    res = []
    for pt in nonzeros:
        tmp = points.copy()
        tmp = [tmp[i] for i in range(len(tmp)) if i not in [pt[0][2], pt[1][2], pt[2][2]]]
        check = []
        for rest in tmp:
            check_tmp = Barycentric(pt[0], pt[1], pt[2], pt[3], rest[0], rest[1])
            check.append(check_tmp)
            if not check_tmp:
                break
        if all(check):
            return [pt[0][2],pt[1][2],pt[2][2]]
    return []
    

def Barycentric(p0, p1, p2, area, px, py):  
    s = 1/(2*area)*(p0[1]*p2[0]-p0[0]*p2[1]+(p2[1]-p0[1])*px+(p0[0]-p2[0])*py)
    t = 1/(2*area)*(p0[0]*p1[1]-p0[1]*p1[0]+(p0[1]-p1[1])*px+(p1[0]-p0[0])*py)

    if (1-s-t==0 and s>0 and t>0) or (s==0 and t>0 and 1-s-t>0) or (t==0 and s>0 and 1-s-t>0):
        return False
    if s > 0 and t > 0 and 1-s-t > 0:
        return False

    return True

def calc_area(p0, p1, p2):
    return 0.5 *(-p1[1]*p2[0]+p0[1]*(-p1[0]+p2[0])+p0[0]*(p1[1]-p2[1])+p1[0]*p2[1])


if __name__ == '__main__':
    print(solution([0, 1, 3, 0, 0, 2], [3, 0, 0, 1, 2, 0]))
