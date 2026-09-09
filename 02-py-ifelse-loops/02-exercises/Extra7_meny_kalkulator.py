while True:
    print("1. Addition")
    print("2. Substraction")
    print("3. Multiplication")
    print("4. Division")
    print("5. Exit")
    choice = int(input("Choose an option: "))
    if choice==5:
        print("ByeBye!")
        break
    elif choice ==1:
        a= int(input("Enter a number: "))
        b = int(input("Enter a number: "))
        print(a+b)
    elif choice ==2:
        a= int(input("Enter a number: "))
        b = int(input("Enter a number: "))
        print(a-b)
    elif choice ==3:
        a= int(input("Enter a number: "))
        b = int(input("Enter a number: "))
        print(a*b)
    elif choice ==4:
        a= int(input("Enter a number: "))
        b = int(input("Enter a number: "))
        if b==0:
            print("you cannot divide by 0")
        else:
            print(a/b)
    else:
        print(f"You chosed: {choice}")
