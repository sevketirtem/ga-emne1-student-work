#Sekunder til timer, minutter og sekunder

seconds = int(input("Enter the seconds: "))

hours = seconds //3600

minutes = seconds % 3600 //60

resten_seconds = seconds % 60

print(f"Hours: {hours}, minutes: {minutes}, secounds: {resten_seconds}.")
