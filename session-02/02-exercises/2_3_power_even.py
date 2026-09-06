number = int(input("Enter a number: "))

second_force = number **2
third_force = number **3

print(f"Second force of the number is {second_force}")
print(f"Third force of the number is {third_force}")

rest_divide_by_2 = number % 2

if rest_divide_by_2 == 0:
    print("Number is even.")
else:
    print("Number is odd.")

