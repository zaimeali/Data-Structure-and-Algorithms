try:
    number = int(input("Enter Number: "))

    for i in range(1, 11):
        print(f"{number} x {i} = {number * i}")
except ValueError:
    print("Input Value is not a Number")
