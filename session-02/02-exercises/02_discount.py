amount = float(input("What is the amount of shopping?:  "))

if amount >= 1000:
    discount_multiplier = 0.8
elif 500 <= amount :
    discount_multiplier = 0.9
else:
    discount_multiplier = 1

discounted_price = amount * discount_multiplier

print(f"Discounted price is {discounted_price:.2f} kr.")
