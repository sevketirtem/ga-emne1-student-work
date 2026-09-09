#Testing user input

name = input("What is your name? ")
course = "Emne 1"

print(f"Hello, {name}!")
print("Hello, "+ name + "!")
print("Hello,", name, "!")

print(f"Welcome to Course {course}.")

age = int(input ("How old are you? "))
next_year = age + 1

print(f"Next year you'll ve {next_year}.")