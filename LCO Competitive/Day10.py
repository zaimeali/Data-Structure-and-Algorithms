if __name__ == '__main__':
    try:
        miles = 2052
        days = 6

        totalMilesPerDay = 2052 / 6
        stopsPerDay = 2
        totalStops = stopsPerDay * days

        print(totalMilesPerDay / stopsPerDay)

    except:
        print('Error')
