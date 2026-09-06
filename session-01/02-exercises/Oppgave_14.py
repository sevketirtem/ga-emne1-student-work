#Enkel valutaomregning

amount = float(input("Enter the amount of the money = "))
exchange_rate = float(input(f"Enter the rate (This is not actual rate. It is just for to test usages.) = "))

converted_money = amount * exchange_rate

print(f"The converted money with rate is= {converted_money} kr.")
