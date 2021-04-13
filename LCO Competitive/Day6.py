if __name__ == '__main__':
    try:
        f = int(input('Free Bytes: '))
        u = int(input('Used Bytes: '))

        o = int(input('Size of file want to delete: '))
        n = int(input('Size of file want to create: '))

        u -= o  # file deleted
        f += o  # free space added

        u += n  # file created
        f -= n  # size consumed

        print(f"Free Size on Floppy Disk is: {f}")

    except:
        print('Error Occured')
