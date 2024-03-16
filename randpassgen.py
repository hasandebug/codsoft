import random

while True:
    length = int(input("Enter Length of your password(Press '0' to exit): "))
    if length == 0:
        break
    else:
        smallalph = "abcdefghijklmnopqrstuvwxyz"
        upperalph = smallalph.upper()
        numbers = "0123456789"
        specialChar = "!@#$%^&*()'<>?[]~`"

        string = smallalph + upperalph + numbers + specialChar
        password = "".join(random.sample(string, length))
        print(password)

print("good bye :)")
