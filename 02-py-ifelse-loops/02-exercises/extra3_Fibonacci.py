user_limit = int(input("Enter a user limit: "))
first = 1
second = 1
print(first)

while second <= user_limit: #for i range (0,8)
    print(second)

    new_number = first + second
    first = second
    second = new_number
