# https://leetcode.com/problems/reverse-integer/

def solution(x):
    neg = False
    if x < 0:
        neg = True
        x = abs(x)

    x = str(x)
    x = x[::-1]
    x = int(x)
    if neg:
        x *= -1

    return x


if __name__ == '__main__':
    num = 123
    print(solution(num))

    num = -123
    print(solution(num))

    num = 120
    print(solution(num))

    num = 0
    print(solution(num))
