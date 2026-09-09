#Mini-prosjekt: Totalpris

product_name = input("Enter the product name: ")
unit_price = float(input("Enter the unit price: "))
amount = int(input("Enter the amount: "))

total_price = unit_price * amount

print(f"The price of the {product_name} is {total_price} kr.")
