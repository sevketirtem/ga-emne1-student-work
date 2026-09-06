secret_pin = 2468
attempts_left = 3
is_authenticated = False

while not is_authenticated and attempts_left > 0:
    pin_code = int(input("Enter pin code: "))
    if pin_code == secret_pin:
        print("Access granted.")
        is_authenticated = True
    else:
        attempts_left -=1
        print(f"Attempt {attempts_left} left")
if attempts_left == 0:
    print("Access denied !")
