from pathlib import Path
print(f"Current directory is: {Path.cwd()}")
data_directory = Path("..") / "data"
#print(data_directory)

prices_path = data_directory / "price.txt"
report_path = data_directory / "price_report.txt"
prices = []

with open(prices_path,"r", encoding="utf-8") as file:
    for line in file:
        prices.append(float(line.strip()))
print(prices)

