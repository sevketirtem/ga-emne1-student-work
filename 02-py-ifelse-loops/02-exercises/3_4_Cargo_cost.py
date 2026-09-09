weight = int(input("Weight of the package: "))


if weight <= 2:
    cargo_cost = 79
    print(f"Cargo cost is {cargo_cost}.")
elif 2 < weight <= 5:
    cargo_cost = 129
    print(f"Cargo cost is {cargo_cost}.")

elif 5 < weight <= 10 :
    cargo_cost = 199
    print(f"Cargo cost is {cargo_cost}.")

else:
    print("Cannot be transported.")
