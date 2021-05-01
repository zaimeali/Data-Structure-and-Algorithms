if __name__ == '__main__':
    try:
        nurse_howard = 8
        nurse_pease = 10
        nurse_campbell = 9
        nurse_grace = 8
        nurse_mccarthy = 7
        nurse_murphy = 12

        avg_hours = (nurse_howard + nurse_pease + nurse_campbell +
                     nurse_grace + nurse_mccarthy + nurse_murphy) / 6

        print(f"Average Number of Hours: {avg_hours}")
    except:
        print('Error Occurred')
