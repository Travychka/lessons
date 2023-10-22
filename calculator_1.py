while True:
    value_operator = input("Please choose an operator: \n 1 '+'\n 2 '-'\n 3 '*'\n 4 '/' \n Q 'to Quit' \n Your answer: ").upper()
    if "1234Q".find(value_operator) == -1:
        print("You have not typed a valid operator.")
        continue
    if value_operator == "Q":
        break

    value_int_1 = int(input("Please type a number: "))
    value_int_2 = int(input("Please type another number: "))
    if value_int_2 == 0 and value_operator == "4":
        print("Can't divide by zero")
        continue

    if value_operator == "1":
        print("Your result:")
        print(value_int_1 + value_int_2)
    elif value_operator == "2":
        print("Your result:")
        print(value_int_1 - value_int_2)
    elif value_operator == "3":
        print("Your result:")
        print(value_int_1 * value_int_2)
    elif value_operator == "4":
        print("Your result:")
        print(value_int_1 / value_int_2)
