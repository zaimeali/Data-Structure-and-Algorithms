# https://projecteuler.net/problem=1

def solution(num):
    res = 0
    for i in range(3, num):
        if i % 3 == 0 or i % 5 == 0:
            res += i
    return res


if __name__ == '__main__':
    num = 10
    print(solution(num))

    num = 1000
    print(solution(num))
