def calculate_discounted_price(price,discount_percent):
    discount = price * (discount_percent/100)
    discounted_price = price - discount
    return discounted_price
price_decreased_1 = calculate_discounted_price(100, 22)
print(f"Discounted Price is: {price_decreased_1:.2f}")

price_decreased_2 = calculate_discounted_price(200, 11)
print(f"Discounted Price is: {price_decreased_2:.2f}")

price_decreased_3 = calculate_discounted_price(500, 50)
print(f"Discounted Price is: {price_decreased_3:.2f}")