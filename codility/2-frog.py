# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")

def solution(blocks):
    # write your code in Python 3.6
    res = []
    for i in range(len(blocks)):
        count = 1
        if i == 0:
            count += count_right(i, blocks)
        elif i == len(blocks) - 1:
            count += count_left(i, blocks)
        else:
            count += count_left(i, blocks)
            count += count_right(i, blocks)
        res.append(count)
    return max(res)

def count_left(i, blocks):
    if i - 1 >= 0 and blocks[i-1] >= blocks[i]:
        return 1  + count_left(i-1, blocks)
    else:
        return 0

def count_right(i, blocks):
    if i+1 <= len(blocks)-1 and blocks[i+1] >= blocks[i]:
        return 1  + count_right(i+1, blocks)
    else:
        return 0

if __name__ == '__main__':
    print(solution([1,5,5,2,6]))
