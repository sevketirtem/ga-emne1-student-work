secret_number = 21
attempts_left = 5
guessed_correctly = False

# While - loop
    #Input from user
    #If-else logic here to handle the possible guesses

# While-loop
# while attempts_left > 0 and guessed_correctly !=True:
while attempts_left > 0 and not guessed_correctly:
    guess = int(input("Guess a number: (1-30)  "))
    if guess == secret_number:
        print("Correct!")
        guessed_correctly = True
    elif guess < secret_number:
        print("Too low!")
    else:
        print("Too high!")
    attempts_left -= 1

if not guessed_correctly:
    print(f"Then number was {secret_number}")