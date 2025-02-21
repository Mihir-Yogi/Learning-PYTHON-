number = 1

is_prime = True

if number > 1:
    for i in range(2, number):
        if (number % i) == 0:
            is_prime = False
            break
else:
    print("Given Number is Incorrect, Please Try again!")
    exit()


print(is_prime)