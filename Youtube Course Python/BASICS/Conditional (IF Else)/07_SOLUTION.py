Coffe = "expresso"
Order = input("Small, Medium, Large ? \n")

Order.lower()

if Order == "small":
    OrderF = "Small"
elif Order == "medium":
    OrderF = "Medium"
elif Order == "large":
    OrderF = "Large"
else:
    print("You Have Spell mistake, please try again!")
    exit()

if Coffe == "expresso":
    Option = input("Do You Want Extra Shot ? Y/N \n")
    Option.lower()
    if Option == "y" or Option == "yes":
        OptionF = "YES"
    elif Option == "n":
        OptionF = "NO"
    else:
        OptionF = "NO"
else:
    OptionF = "NO"


print("Coffe type is : ",Coffe ,"\nSize is : ",OrderF, "\nExtra Shot :",OptionF)