def greatestCommonFactor(white_blood, red_blood):
    return white_blood if red_blood == 0 else greatestCommonFactor(red_blood, white_blood % red_blood)


def solution(red_blood, white_blood):
    factor = greatestCommonFactor(white_blood, red_blood)
    whiteRatio = white_blood // factor
    redRatio = red_blood // factor

    print(f"Ratio {whiteRatio}:{redRatio}")


if __name__ == '__main__':
    red_blood = 5000000
    white_blood = 8000

    ratio = red_blood / white_blood
    print(f"Ratio is {ratio}")
    solution(red_blood, white_blood)
