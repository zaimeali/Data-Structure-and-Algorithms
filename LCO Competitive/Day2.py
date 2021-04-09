def print_triangle(n):
    for i in range(n + 1):
        for j in range(i, n):
            print(" ", end=" ")
        for j in range(i):
            print("* *")
        for j in range(i):
            print("* *", end=" ")
        # for j in range(i, n):
        #     print(" ", end=" ")
        # for j in range(i):
        #     print("* *")
        print()


def print_stair1(n):
    m = n * 2
    half1 = n - 1
    half2 = n
    for i in range(n):
        for j in range(m):
            # if j == half1:
            #     print(j, end=" ")
            # if j == half2:
            #     print(j, end=" ")
            if half1 > j:
                print(" ", end=" ")
            if j == half1:
                print(j, end=" ")
            if half1 < j < half2:
                print(j, end=" ")
            if j == half2:
                print(j, end=" ")
            # if j == half1:
            #     print(j, end=" ")
            # if half1 < j < half2:
            #     print(j, end=" ")
            # if j == half2:
            #     print(j)
            # if half1 > j:
            #     print(" ", end=" ")
            # if j != half1 and j != half2:
            #     print(" ", end=" ")

        half1 -= 1
        half2 += 1
        print()
    # print(m)


def print_stair(n):
    m = n * 2
    half = m // 2
    a = half
    b = half
    for i in range(n):
        for j in range(m):
            if b >= j >= a:
                print("*", end=" ")
                print("*", end=" ")
            else:
                print(" ", end=" ")
                print(" ", end=" ")
        print()
        for j in range(m):
            if b >= j >= a:
                print("*", end=" ")
                print("*", end=" ")
            else:
                print(" ", end=" ")
                print(" ", end=" ")
        a = a - 1
        b = b + 1
        print()


if __name__ == '__main__':
    # print_triangle(5)
    # print_stair1(5)
    print_stair(5)
