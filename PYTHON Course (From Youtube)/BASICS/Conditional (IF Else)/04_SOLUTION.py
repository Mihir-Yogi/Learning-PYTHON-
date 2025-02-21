Fruit = "Chiiku"
Color = "Purple"
if Fruit == "Banana":
    if Color == "Green":
        State = "Unripe"
    elif Color == "Yellow":
        State = "Ripe"
    elif Color == "Brown":
        State = "Overripe"
    else:
        print("Wrong Color Reading!")
        exit()
else:
    print("Given FruitChecker is Not Available!")
    exit()

print("The", Fruit ,"is", State)