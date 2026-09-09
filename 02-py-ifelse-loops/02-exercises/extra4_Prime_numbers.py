number = int(input("Enter a number: "))
is_prime = True
if number==1:
    print("this is not prime")
else:
    for i in range (2, number):
        if number%i==0:
            is_prime = False
    if not is_prime:
        print("This number is not prime.")
    else:
        print("This number is   prime.")



