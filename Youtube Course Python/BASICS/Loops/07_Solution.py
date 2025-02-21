while True:
    val = int(input("Enter Value between 1 to 10 : "))

    if 1 <= val <= 10:
        print("Thanks!")
        break
    else:
        print("Incorrect input, please try again!")