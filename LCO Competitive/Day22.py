if __name__ == '__main__':
    year = int(input("Enter Year: "))
    if year % 4 == 0:
        print(f"{year} is a leap year")
    else:
        print(f"{year} is not a leap year")
