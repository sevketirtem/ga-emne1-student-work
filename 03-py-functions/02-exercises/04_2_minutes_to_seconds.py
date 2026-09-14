def convert_minutes_to_seconds(minutes):
    seconds = minutes * 60
    return seconds

converted_1 = convert_minutes_to_seconds(1)
print(f"Converted seconds are : {converted_1}")

converted_2 = convert_minutes_to_seconds(2.5)
print(f"Converted seconds are : {converted_2}")

converted_10 = convert_minutes_to_seconds(10)
print(f"Converted seconds are : {converted_10}")