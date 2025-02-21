age = input("Enter Your Age: ")
age_int = int(age)

if age_int < 13:
    print("You are Child!")
elif age_int < 20:
    print("You are Teenager!")
elif age_int < 60:
    print("You are Adult!")
else:
    print("You are Senior!")