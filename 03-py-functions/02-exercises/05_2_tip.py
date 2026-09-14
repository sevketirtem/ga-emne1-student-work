def calculate_tip(amount, tip_percent=0):
    tips_amount = amount * (tip_percent/100)
    return tips_amount
print(calculate_tip(100))
print(calculate_tip(200,10))