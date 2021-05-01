# Hours = 12, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11
# Minutes = 00 - 60

# Minute Logic
# print(30 // 5)

def mySolution(hours, minutes):
    if hours < 0 or minutes < 0 or hours > 12 or minutes > 60:
        return 'Wrong Input'

    if hours == 12:
        hours = 0

    if minutes == 60:
        minutes = 0

    angle = 0

    while hours != (minutes // 5):
        angle += 15
        hours += 0.5

        if hours == 12:
            hours = 0

    return angle


if __name__ == '__main__':
    hours = int(input('Enter Hours: '))
    minutes = int(input("Enter Minutes: "))

    angle = mySolution(hours, minutes)
    print(f"Angle is {angle}")
