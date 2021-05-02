if __name__ == '__main__':
    num = int(input("Enter Number: "))
    # num % 2 = 0 or 1
    # remainder = num % 2
    # division = num // 2

    binary = []

    divisible = num

    while True:
        remainder = divisible % 2
        binary.append(remainder)
        divisible = divisible // 2
        if divisible == 1:
            binary.append(divisible)
            break

    binary.reverse()
    print(binary)

    answer = "".join([str(b) for b in binary])
    print(f"Binary value of {num} is {answer}")
