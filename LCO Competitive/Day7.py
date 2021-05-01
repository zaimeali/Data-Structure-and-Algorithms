if __name__ == '__main__':
    try:
        eachDay = 1200000
        numberOfYears = int(input('Enter years: '))
        days = numberOfYears * 365

        peopleInYears = 0

        for i in range(days):
            peopleInYears += eachDay

        print(peopleInYears)

    except:
        print('Error Occured')
