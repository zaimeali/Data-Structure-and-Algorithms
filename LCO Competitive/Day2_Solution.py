def pattern(n):
    for i in range(1, n+1):                    # 1 -> 11
        k = i + 1 if (i % 2 != 0) else i       # k = 2

        for g in range(k, n):                  # 2 -> 10, g = 2
            if g >= k:                         # 2 >= 2
                print(end=" ")
        for j in range(0, k):                  # 0 -> 2
            if j == k - 1:                     # 0 == 2 - 1
                print("*")
            else:
                print("*", end=" ")


if __name__ == "__main__":
    n = 10
    pattern(n)
