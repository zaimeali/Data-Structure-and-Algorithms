def square(num):
    sum = 0
    for i in range(0, num):
        sum += num

    print(sum)


if __name__ == '__main__':
    num = int(input("Enter Number: "))
    print(num**2)
    square(num)
