# First Recurring Character
# Input ABCA -> return A
# Input BDCBDA -> return B
# Input BCA -> return None

# ref video -> https://www.youtube.com/watch?v=GJdiM-muYqc

def first_recurring(given_string):
    check = {}
    for char in given_string:
        if char in check:
            return char
        check[char] = 'Exist'
    return None


if __name__ == '__main__':
    try:
        # test = 'ABCA'
        test = 'BDCBDA'
        recurring = first_recurring(test)
        print(f"Recurring Character is: {recurring}")
    except:
        print('Error Occured')
