#Whitout notes- pure version
def print_error(message, prefix="Error: "):
    print(f"{prefix}{message}")

def is_valid_integer(text):
    if text == "":
        return False
    if text[0]=="-":
        digits_part = text[1:]
    else:
        digits_part = text

    if digits_part =="":
        return False
    for character in digits_part:
        if character < "0" or character > "9":
            return False
    return True

def get_positive_integer(prompt):
    valid = False
    value = 0

    while not valid:
        text = input(prompt)

        if is_valid_integer(text):
            value = int(text)

            if value > 0:
                valid = True
            else:
                print_error("The number must be positive (greater than 0). Try again.")
        else:
            print_error("Invalid input. Please enter a whole number.")
    return value

def calculate_used_time():
    print("\n--- Calculate Used Time ---\n")

    number_of_studies = get_positive_integer("Enter the number of the studies:  ")
    length_of_each_study = get_positive_integer("Enter the length of each study in minutes: ")

    hour_total_time_used = (number_of_studies * length_of_each_study) // 60
    minutes_total_time_used = (number_of_studies * length_of_each_study) % 60
    total_time_used = (f"{hour_total_time_used } hours and {minutes_total_time_used} minutes")
    print(f"The total time has been used: {total_time_used}")

calculate_used_time()