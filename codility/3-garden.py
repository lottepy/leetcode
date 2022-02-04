# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")

def solution(A):
    # write your code in Python 3.6
    if check_aesthetical(A):
        return 0
    else:
        count = 0
        for i in range(len(A)):
            tmp = A.copy()
            del tmp[i]
            if check_aesthetical(tmp):
                count += 1
        if count > 0:
            return count
        else:
            return -1    

def check_aesthetical(l):
    tmp = all(cmp(a, b)*cmp(b, c) == -1 for a, b, c in zip(l, l[1:], l[2:]))
    return tmp

def cmp(a,b):
    return (a>b) - (a<b)

if __name__ == '__main__':
    print(solution([3,4,5,3,7]))
