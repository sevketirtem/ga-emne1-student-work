def calculate_total (price,quantity):
    total = price * quantity
    return total


order_total = calculate_total(149.5,3)
print(f"Total: {order_total:.2f}")
