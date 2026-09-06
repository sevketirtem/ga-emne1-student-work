first_number = int(input("Enter first number: "))
second_number= int(input("Enter second number: "))

# in case of 0 value for second number, program CRASHED !
if second_number == 0:
    print("You cannot divide by zero !")
else:
    sum = first_number + second_number
    substraction = first_number -second_number
    multiplication = first_number * second_number
    division_normal = first_number / second_number
    division_integer = first_number // second_number
    division_rest = first_number % second_number

    print(f"Sum:            {sum}")
    print(f"Substraction:   {substraction}")
    print(f"Maltiplication: {multiplication}")
    print(f"Division Normal:{division_normal:.2f}")
    print(f"Division Integer:{division_integer}")
    print(f"Division Rest:   {division_rest}")