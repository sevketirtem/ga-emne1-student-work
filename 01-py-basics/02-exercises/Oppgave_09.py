#COnvert minute second
minute = float(input("Enter the number of the minute= "))
hour = int(minute//60)
resten_minute = int(minute%60)

print(f"hour= {hour}, minute= {resten_minute}")