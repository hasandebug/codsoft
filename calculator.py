while True:
    print(
        "\nWhich operation you want to perform?\n"
        " Press 1 to Add\n"
        " Press 2 to Subtract\n"
        " Press 3 to Multiply\n"
        " Press 4 to Divide\n"
        " Press 0 to Exit\n"
    )
    options = input("Enter Here: ")
    if options == "0":
        break
    else:
        options = int(options)

    print("Enter your first number (or 'e' to exit):")
    num1 = input()
    if num1 == "e" or num1 == "E":
        break
    else:
        num1 = float(num1)

    print("Enter your second number (or 'e' to exit):")
    num2 = input()
    if num2 == "e" or num2 == "E":
        break
    else:
        num2 = float(num2)

    add = num1 + num2
    subtract = num1 - num2
    multiply = num1 * num2
    divide = num1 / num2

    match options:
        case 1:
            print("Addition Result: %f" % add)
        case 2:
            print("Subtraction Result: %f" % subtract)
        case 3:
            print("Multiplication Result: %f" % multiply)
        case 4:
            if num2 != 0:
                print("Division Result: %f" % divide)
            else:
                print("Doesn't exist")

print("Exiting the program.")
