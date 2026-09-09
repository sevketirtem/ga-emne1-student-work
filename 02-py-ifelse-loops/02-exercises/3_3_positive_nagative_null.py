number = int(input("Enter a number: "))

if number > 0:
    print("The number is positive.")
elif number < 0:
    print("The number is negative.")
else:
    print("The number is 0")

if number != 0:
    odd_even = number % 2
    if odd_even == 0:
        print("The number is even.")
    else:
        print("The number is odd.")