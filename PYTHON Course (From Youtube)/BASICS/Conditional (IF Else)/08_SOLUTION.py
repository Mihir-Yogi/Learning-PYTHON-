password = input("Enter Password : ")
passLen = len(password)

if passLen < 6:
    print("Weak")
elif passLen <= 10:
    print("Medium") 
else:
    print("Strong")