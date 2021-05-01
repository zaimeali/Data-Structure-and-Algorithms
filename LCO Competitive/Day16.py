if __name__ == "__main__":
    sum = 0
    n = input("Enter Number: ")
    for char in n:
        sum += int(char)

    print(f"Sum is {sum}")
