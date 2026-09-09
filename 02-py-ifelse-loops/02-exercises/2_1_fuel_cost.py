distance = float(input("Enter the distance:"))
fuel_per_100_km = float(input("Enter the consumption liter of fuel per 100km: "))
fuel_price_per_liter = float(input("Enter the fuel price in kron per liter: "))

consumption = (distance/100) * fuel_per_100_km

cost = consumption * fuel_price_per_liter

print(f"Total consumption for the trip is {consumption:.2f}lt")
print(f"Total cost for this trip is {cost:.2f}kr")