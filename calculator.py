result = None
error_numbers_only = "It should be a number"

try:
    value_int_1 = int(input("Please type a number: "))
except ValueError:
    print(error_numbers_only)
    value_int_1 = int(input("Please type a number: "))

try:
    value_int_2 = int(input("Please type another number: "))
except ValueError:
    print(error_numbers_only)
    value_int_2 = int(input("Please type another number: "))

value_operator = input("Please choose an operator: \n 1 '+'\n 2 '-'\n 3 '*'\n 4 '/' \nYour answer: ")

if value_operator == "1":
    result = value_int_1 + value_int_2
elif value_operator == "2":
    result = value_int_1 - value_int_2
elif value_operator == "3":
    result = value_int_1 * value_int_2
elif value_operator == "4":
    result = value_int_1 / value_int_2
else:
    print("You have not typed a valid operator, please run the program again.")

print(result)