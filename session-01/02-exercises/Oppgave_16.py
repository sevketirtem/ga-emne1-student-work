#Pris med rabatt

product_price = float(input("Enter the product price: "))
discount_rate = float(input("Enter the discount rate: "))/100

discount = product_price * discount_rate
discounted_price = product_price - discount

print(f"The discount is: {discount:.2f}, the discounted price is: {discounted_price:.2f} kr.")
